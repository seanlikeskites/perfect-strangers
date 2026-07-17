# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, NumpyRounds, ParticipantLabels
from perfect_strangers.util import finite_field_elements, least_prime_factor, submatrix_transpositions


def use_finite_plane_construction(groups_per_round: int, group_size: int) -> bool:
    prime_power_test = galois.is_prime_power(groups_per_round)
    group_size_upper_bound = group_size <= groups_per_round

    lpf = least_prime_factor(groups_per_round)
    group_size_lower_bound = lpf is not None and group_size > lpf

    return prime_power_test and group_size_upper_bound and group_size_lower_bound

def _match_on_finite_plane(participants: np.typing.NDArray, stride: int=1) -> NumpyRounds:
    n_blocks = participants.shape[0] // stride
    group_size = participants.shape[1]

    if n_blocks < group_size:
        return [participants]

    labels = [participants[b::stride, :].transpose() for b in range(stride)]
    field_elements, _ = finite_field_elements(n_blocks)

    rounds = []

    for m in field_elements:
        new_round = [
            [l[x, m * field_elements[x] + c] for x in range(l.shape[0])]
            for c in field_elements
            for l in labels
        ]

        rounds.append(new_round)

    return [np.array(r) for r in rounds]

class FinitePlaneMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _generate_rounds(self):
        participants = self._group_matrices[0].copy()
        self._group_matrices = _match_on_finite_plane(participants)

        # Apply submatrix transposition.
        # For square matrices, transposition is equivalent to using the vertical lines of the finite plane.
        transpositions = submatrix_transpositions(participants)

        for t, s in transpositions:
            self._group_matrices += _match_on_finite_plane(t, s)

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return cls(groups_per_round, group_size, participant_labels)

        return None
