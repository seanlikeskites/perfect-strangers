# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels, RoundSequence
from perfect_strangers.util import finite_field_elements, least_prime_factor, submatrix_transpositions


def use_finite_plane_construction(groups_per_round: int, group_size: int) -> bool:
    prime_power_test = galois.is_prime_power(groups_per_round)
    group_size_upper_bound = group_size <= groups_per_round

    lpf = least_prime_factor(groups_per_round)
    group_size_lower_bound = lpf is not None and group_size > lpf

    return prime_power_test and group_size_upper_bound and group_size_lower_bound

def _match_on_finite_plane(groups_per_round: int, group_size: int, labels: np.typing.NDArray) -> RoundSequence:
    field_elements, _ = finite_field_elements(groups_per_round)

    rounds = []

    for m in field_elements:
        new_round = [
            [labels[x, m * field_elements[x] + c] for x in range(group_size)]
            for c in field_elements
        ]

        rounds.append(new_round)

    return [np.array(r) for r in rounds]

class FinitePlaneMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        super().__init__(groups_per_round, group_size, participant_labels)

    def _generate_rounds(self):
        labels = np.arange(self.n_participants).reshape(self.group_size, self.groups_per_round)
        self._group_matrices = _match_on_finite_plane(self.groups_per_round, self.group_size, labels)

        # Apply submatrix transposition.
        # For square matrices, transposition is equivalent to using the vertical lines of the finite plane.
        transpositions = submatrix_transpositions(self._group_matrices[0])

        for t, _ in transpositions:
            self._group_matrices.append(t)

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return FinitePlaneMatcher(groups_per_round, group_size, participant_labels)

        return None
