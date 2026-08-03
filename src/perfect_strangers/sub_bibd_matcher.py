# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import math

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.design_types import DesignType, RBIBDType
from perfect_strangers.types import GroupingMatrix, ParticipantLabels, RoundSequence
from perfect_strangers.util import round_to_lists, round_to_sets


def _resolvable_orthogonal_array(N: int, k: int, v: int, t: int):
    # Constructing resolvable orthogonal arrays is a whole problem in itself.
    # For now, hard coding solutions for the following values.
    if N == 9 and k == 3 and v == 3 and t == 2:
        return [
            [
                [0, 0, 0],
                [1, 1, 2],
                [2, 2, 1]
            ],
            [
                [0, 1, 1],
                [1, 2, 0],
                [2, 0, 2]
            ],
            [
                [0, 2, 2],
                [1, 0, 1],
                [2, 1, 0]
            ]
        ]

    if N == 16 and k == 3 and v == 4 and t == 2:
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

    if N == 16 and k == 4 and v == 4 and t == 2:
        return [
            [
                [0, 0, 0, 0],
                [1, 3, 2, 1],
                [2, 1, 3, 2],
                [3, 2, 1, 3],
            ],
            [
                [0, 1, 1, 1],
                [1, 2, 3, 0],
                [2, 0, 2, 3],
                [3, 3, 0, 2],
            ],
            [
                [0, 2, 2, 2],
                [1, 1, 0, 3],
                [2, 3, 1, 0],
                [3, 0, 3, 1],
            ],
            [
                [0, 3, 3, 3],
                [1, 0, 1, 2],
                [2, 2, 0, 1],
                [3, 1, 2, 0],
            ]
        ]

    if N == 25 and k == 4 and v == 5 and t == 2:
        return [
            [
                [0, 0, 0, 0],
                [1, 1, 2, 3],
                [2, 2, 4, 1],
                [3, 3, 1, 4],
                [4, 4, 3, 2]
            ],
            [
                [0, 1, 1, 1],
                [1, 2, 3, 4],
                [2, 3, 0, 2],
                [3, 4, 2, 0],
                [4, 0, 4, 3]
            ],
            [
                [0, 2, 2, 2],
                [1, 3, 4, 0],
                [2, 4, 1, 3],
                [3, 0, 3, 1],
                [4, 1, 0, 4]
            ],
            [
                [0, 3, 3, 3],
                [1, 4, 0, 1],
                [2, 0, 2, 4],
                [3, 1, 4, 2],
                [4, 2, 1, 0]
            ],
            [
                [0, 4, 4, 4],
                [1, 0, 1, 2],
                [2, 1, 3, 0],
                [3, 2, 0, 3],
                [4, 3, 2, 1]
            ]
        ]

    return None

def _subtract_S_prime(S_j: GroupingMatrix, S_prime: RoundSequence):
    S_j_set = round_to_sets(S_j)

    for S_prime_j in S_prime:
        S_prime_j_set = round_to_sets(S_prime_j)

        if S_prime_j_set <= S_j_set:
            return round_to_lists(S_prime_j_set), round_to_lists(S_j_set - S_prime_j_set)

    return None, None

def _process_sub_bibd(S: BaseMatcher, v2: int, k: int):
    S_prime: RoundSequence
    V: RoundSequence
    W: RoundSequence

    if v2 > 1:
        # Get SubBIBD
        sub_S = S.sub_matcher(v2 // k)

        if sub_S is None or not isinstance(sub_S.design_type(), RBIBDType):
            return None

        S_prime = []
        V = []
        W = []

        for S_j in S.rounds:
            S_prime_j, V_j = _subtract_S_prime(S_j, sub_S.rounds)

            if V_j is not None:
                S_prime.append(S_prime_j)
                V.append(V_j)
            else:
                W.append(S_j)

    else:
        S_prime = []
        V = []
        W = S.rounds

    return {
        "S_prime": S_prime,
        "V": V,
        "W": W
    }


def _construction_elements(v1: int, v2: int, m: int, k: int, tried_sub_bibds: list[tuple[int, int]]):
    """
    Create elements necessary for construction using Theorem 4 from Ray-Chaudhuri and Wilson (1971).

    :return: Returns None if not all necessary elements exist, otherwise returns a dict with the following elements:
               * v1
               * v2
               * m
               * B: a (v1, k, 1)-RBIBD
               * S: a ((k - 1)m + v2, k, 1)-RBIBD
               * S_prime: a (v2, k, 1)-SubRBIBD of S
               * V: parallel classes of S which are supersets of the parallel classes of S_prime, with
                    the corresponding parrallel class of S_prime removed
               * W: parallel classes of S which are not supersets of the parallel classes of S_prime
               * roa: a (k, m, 2, 1)-resolvable orthogonal array
    """
    from perfect_strangers.factory import matcher_factory

    if v1 % k != 0:
        return None

    S_size = (k - 1) * m + v2

    if S_size % k != 0:
        return None

    B = matcher_factory(v1 // k, k, tried_sub_bibds=tried_sub_bibds)

    if not isinstance(B.design_type(), RBIBDType):
        return None

    S = matcher_factory(S_size // k, k, tried_sub_bibds=tried_sub_bibds)

    if not isinstance(S.design_type(), RBIBDType):
        return None

    S_parts = _process_sub_bibd(S, v2, k)

    if S_parts is None:
        return None

    roa = _resolvable_orthogonal_array(m * m, k, m, 2)

    if roa is None:
        return None

    return {
        "v1": v1,
        "v2": v2,
        "m": m,
        "B": B.rounds,
        "S": S.rounds,
        "roa": roa
    } | S_parts

class SubBIBDMatcher(BaseMatcher):
    """
    Theorem 4 from Ray-Chaudhuri and Wilson (1971).
    """
    def __init__(self,
                 v1: int,
                 v2: int,
                 m: int,
                 B: RoundSequence,
                 S: RoundSequence,
                 S_prime: RoundSequence,
                 V: RoundSequence,
                 W: RoundSequence,
                 roa: RoundSequence,
                 participant_labels: ParticipantLabels=None):
        self._v1 = v1
        self._v2 = v2
        self._m = m
        self._B = B
        self._S = S
        self._S_prime = S_prime
        self._V = V
        self._W = W
        self._roa = roa

        group_size = len(B[0][0])
        groups_per_round = (m * (v1 - 1) + v2) // group_size

        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _treatment_set(self, X: list[int]):
        """
        Return the participant IDs corresponding to the treatment set X × I_m + Y.
        """
        return [(x, y) for x in X for y in self._I_m] + self._Y

    def _groups_from_S_j(self, S_j: GroupingMatrix, B_i: GroupingMatrix):
        B_i_prime = next([p for p in b if p != self._theta] for b in B_i if self._theta in b)
        treatment = self._treatment_set(B_i_prime)

        treatment_map = {
            t: treatment[i]
            for i, t in enumerate(sorted(t for g in S_j for t in g if t not in self._Y))
        } | {
            y: y
            for y in self._Y
        }

        return [
            [self._treatment_participant_map[treatment_map[t]] for t in g]
            for g in S_j
        ]

    def _groups_from_S_prime_j(self, S_prime_j: GroupingMatrix):
        return [
            [self._treatment_participant_map[t] for t in g]
            for g in S_prime_j
        ]

    def _sub_rbibd_round(self, j: int):
        """
        Construct a round based on the first part of the construction starting in the middle of page 194 of Ray-Chaudhuri
        and Wilson (1971). The rounds are those given by E_j in the paper.
        """
        groups = self._groups_from_S_prime_j(self._S_prime[j])

        V_j = self._V[j]

        for B_i in self._B:
            groups += self._groups_from_S_j(V_j, B_i)

        return groups

    def _roa_round(self, i: int, j: int):
        """
        Construct a round based on the second part of the construction starting at the bottom of page 194 of Ray-Chaudhuri
        and Wilson (1971). The rounds are those given by E^i_j in the paper.
        """
        B_i = self._B[i]
        B = [b for b in B_i if self._theta not in b]

        P_j = self._roa[j]

        P_j_of_B = [
            [self._treatment_participant_map[(x, y)] for x, y in zip(b, p, strict=False)]
            for b in B
            for p in P_j
        ]

        W_j = self._W[j]

        W_i_j = self._groups_from_S_j(W_j, B_i)

        return P_j_of_B + W_i_j

    def _generate_rounds(self):
        self._theta = self._v1 - 1
        self._X_prime = list(range(self._theta))
        self._I_m = list(range(self._m))

        if self._v2 > 1:
            self._Y = [t for g in self._S_prime[0] for t in g]
        else:
            self._Y = [self._theta]

        treatment_set = self._treatment_set(self._X_prime)

        self._treatment_participant_map = {
            t: i for i, t in enumerate(treatment_set)
        }

        rounds = []

        # Construct rounds from sub-RBIBD.
        for j in range(len(self._S_prime)):
            rounds.append(self._sub_rbibd_round(j))

        # Construct rounds from orthogonal array.
        for i in range(len(self._B)):
            for j in range(self._m):
                rounds.append(self._roa_round(i, j))

        self._group_matrices = [np.array(r) for r in rounds]

    def _design_type(self) -> DesignType:
        return RBIBDType(self.n_participants, self.group_size)

    def _available_sub_matchers(self) -> set[int]:
        sizes = {
            (self._m * (self.group_size - 1) + self._v2) // self.group_size
        }

        sizes = set()

        if self._v2 > 1:
            sizes.add(self._v2 // self.group_size)

        return sizes

    def _sub_matcher(self, groups_per_round: int) -> BaseMatcher | None:
        n_participants = groups_per_round * self.group_size

        if n_participants == self._v2:
            sequence = [
                self._groups_from_S_prime_j(S_prime_j)
                for S_prime_j in self._S_prime
            ]
        elif n_participants == self._m * (self.group_size - 1) + self._v2:
            sequence = [
                self._groups_from_S_j(S_j, self._B[0])
                for S_j in self._S
            ]
        else:
            return None

        return BaseMatcher(round_sequence=sequence)

    @classmethod
    def create_matcher(cls,
                       groups_per_round: int,
                       group_size: int,
                       tried_sub_bibds: list[tuple[int, int]],
                       participant_labels: ParticipantLabels=None):
        n_participants = groups_per_round * group_size

        v2 = 1

        while v2 < n_participants:
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

            v2 *= group_size

        return None
