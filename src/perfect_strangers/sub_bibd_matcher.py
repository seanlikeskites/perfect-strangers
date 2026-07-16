# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import math

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels, RoundGroups


def _resolvable_orthogonal_array(m: int, n: int, d: int, lambd: int):
    # Constructing resolvable orthogonal arrays is a whole problem in itself.
    # For now, hard coding a solution for the following values.
    # This will allow for construction using Theorem 4 where m=4 and v2=1.
    if m == 3 and n == 4 and d == 2 and lambd == 1:
        return [
            [
                [0, 0, 0],
                [1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]
            ],
            [
                [0, 1, 1],
                [1, 3, 2],
                [2, 2, 0],
                [3, 0, 3]
            ],
            [
                [0, 2, 2],
                [1, 0, 1],
                [2, 1, 3],
                [3, 3, 0]
            ],
            [
                [0, 3, 3],
                [1, 1, 0],
                [2, 0, 2],
                [3, 2, 1]
            ]
        ]

    return None

def _is_bibd(matcher: BaseMatcher):
    return matcher.max_rounds == (matcher.n_participants - 1) / (matcher.group_size - 1)

def _construction_elements(v1: int, v2: int, m: int, k: int, tried_sub_bibds: list[tuple[int, int]]):
    """
    Create elements necessary for construction according using Theorem 4 from Ray-Chaudhuri and Wilson (1971).

    :return: Returns None if not all necessary elements exist, otherwise returns a dict with the following elements:
               * v1
               * v2
               * m
               * B: a (v1, k, 1)-RBIBD
               * S: a ((k - 1)m + v2, k, 1)-RBIBD
               * roa: a (k, m, 2, 1)-resolvable orthogonal array
    """
    from perfect_strangers.factory import matcher_factory

    if v1 % k != 0:
        return None

    S_size = (k - 1) * m + v2

    if S_size % k != 0:
        return None

    B = matcher_factory(v1 // k, k, tried_sub_bibds=tried_sub_bibds)

    if not _is_bibd(B):
        return None

    S = matcher_factory(S_size // k, k, tried_sub_bibds=tried_sub_bibds)

    if not _is_bibd(S):
        return None

    roa = _resolvable_orthogonal_array(k, m, 2, 1)

    if roa is None:
        return None

    return {
        "v1": v1,
        "v2": v2,
        "m": m,
        "B": B.rounds,
        "S": S.rounds,
        "roa": roa
    }

class SubBIBDMatcher(BaseMatcher):
    """
    Theorem 4 from Ray-Chaudhuri and Wilson (1971).
    """
    def __init__(self, v1: int, v2: int, m: int, B: list[RoundGroups], S: list[RoundGroups], roa, participant_labels: ParticipantLabels=None):
        self._v1 = v1
        self._v2 = v2
        self._m = m
        self._B = B
        self._S = S
        self._roa = roa

        group_size = len(B[0][0])
        groups_per_round = (m * (v1 - 1) + v2) // group_size

        super().__init__(groups_per_round, group_size, participant_labels)

    def _participant_id_from_treatment(self, x: int, i: int):
        """
        Return the participant ID corresponding to a given treatment from the set X' × I_m.

        :param x: The element from X
        :param i: The element from I_m
        """

        return i * self._theta + x

    def _treatment_set(self, X: list[int]):
        """
        Return the participant IDs corresponding to the treatment set X × I_m + Y.
        """
        return [self._participant_id_from_treatment(x, y) for x in X for y in self._I_m] + self._Y

    def _roa_round(self, i: int, j: int):
        """
        Construct a round based on the second part of the construction starting at the bottom of page 194 of Ray-Chaudhuri
        and Wilson (1971). The rounds are those given by E_j_i in the paper.
        """
        B_i = self._B[i]
        B = [b for b in B_i if self._theta not in b]
        B_prime = next([p for p in b if p != self._theta] for b in B_i if self._theta in b)

        P_j = self._roa[j]

        P_j_i = [
            [self._participant_id_from_treatment(x, y) for x, y in zip(b, p, strict=False)]
            for b in B
            for p in P_j
        ]

        S_j = self._S[j]
        S_treatment = self._treatment_set(B_prime)

        S_j_i =  [
            [S_treatment[i] for i in r]
            for r in S_j
        ]

        return P_j_i + S_j_i

    def _generate_rounds(self):
        self._theta = self._v1 - 1
        self._Y = list(range(self._theta * self._m, self._theta * self._m + self._v2))
        self._I_m = list(range(self._m))

        rounds = []

        # One would construct the parallel classes E_j here if v2 > 1.

        for i in range(len(self._B)):
            for j in range(self._m):
                rounds.append(np.array(self._roa_round(i, j)))

        self._group_matrices = rounds


    @classmethod
    def create_matcher(cls,
                       groups_per_round: int,
                       group_size: int,
                       tried_sub_bibds: list[tuple[int, int]],
                       participant_labels: ParticipantLabels=None):
        n_participants = groups_per_round * group_size

        # For now assume v2 is 1 because I have no idea how to construct BIBDs with sub-BIBDs.
        v2 = 1

        m_by_v1_less_1 = n_participants - v2

        for candidate_1 in range(2, int(math.sqrt(m_by_v1_less_1))):
            if m_by_v1_less_1 % candidate_1:
                continue

            candidate_2 = m_by_v1_less_1 // candidate_1

            elements = _construction_elements(candidate_2 + 1, v2, candidate_1, group_size, tried_sub_bibds)

            if elements is None:
                elements = _construction_elements(candidate_1 + 1, v2, candidate_2, group_size, tried_sub_bibds)

            if elements is None:
                continue

            return cls(**elements, participant_labels=participant_labels)

        return None
