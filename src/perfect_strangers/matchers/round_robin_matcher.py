# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy as np

from perfect_strangers.design_types import DesignType, RBIBDType
from perfect_strangers.matchers.base_matcher import BaseMatcher
from perfect_strangers.types import NumpyRounds


class RoundRobinMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, participant_labels: Sequence | None=None):
        # Round robin matching works with a group size of 2.
        super().__init__(groups_per_round, 2, participant_labels=participant_labels)

    def _generate_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        def _rotate_groups(g):
            flat = g.flatten("F")
            flat[1:self.groups_per_round] = np.flip(flat[1:self.groups_per_round])
            flat[1:] = np.roll(flat[1:], 1)
            flat[1:self.groups_per_round] = np.flip(flat[1:self.groups_per_round])
            return flat.reshape(g.shape, order="F")

        rounds = [initial_groupings]

        for _ in range(self.n_participants - 2):
            rounds.append(_rotate_groups(rounds[-1]))

        return rounds

    def _design_type(self) -> DesignType:
        return RBIBDType(self.n_participants, 2)
