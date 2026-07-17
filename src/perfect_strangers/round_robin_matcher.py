# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels
from perfect_strangers.design_types import DesignType, RBIBDType


class RoundRobinMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, participant_labels: ParticipantLabels=None):
        # Round robin matching works with a group size of 2.
        super().__init__(groups_per_round, 2, participant_labels=participant_labels)

    def _generate_rounds(self):
        def _rotate_groups(g):
            flat = g.flatten("F")
            flat[1:self.groups_per_round] = np.flip(flat[1:self.groups_per_round])
            flat[1:] = np.roll(flat[1:], 1)
            flat[1:self.groups_per_round] = np.flip(flat[1:self.groups_per_round])
            return flat.reshape(g.shape, order="F")

        for _ in range(self.n_participants - 2):
            self._group_matrices.append(_rotate_groups(self._group_matrices[-1]))

    def _design_type(self) -> DesignType:
        return RBIBDType(self.n_participants, 2)
