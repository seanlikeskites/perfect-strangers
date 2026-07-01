# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels
from perfect_strangers.util import finite_field_elements


class FinitePlaneMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        super().__init__(groups_per_round, group_size, participant_labels)

    def _generate_rounds(self):
        labels = np.arange(self.n_participants).reshape(self.group_size, self.groups_per_round)

        field_elements, _ = finite_field_elements(self.groups_per_round)

        rounds = []

        for m in field_elements:
            new_round = [
                [labels[x, m * field_elements[x] + c] for x in range(self.group_size)]
                for c in field_elements
            ]

            rounds.append(new_round)

        # For a square matrix we can use every line in the finite affine plane.
        if self.groups_per_round == self.group_size:
            new_round = [
                [labels[x, y] for y in field_elements]
                for x in field_elements
            ]

            rounds.append(new_round)

        self._group_matrices = [np.array(r) for r in rounds]

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return FinitePlaneMatcher(groups_per_round, group_size, participant_labels)

        return None
