# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy as np

from perfect_strangers.matchers.base_matcher import BaseMatcher
from perfect_strangers.types import GroupSpec, NumpyRounds


class TypedMatcher(BaseMatcher):
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 participant_labels: Sequence | None=None):

        self.group_spec = list(group_spec)
        group_size = sum(group_spec)

        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _generate_typed_rounds(self, _initial_groupings: np.typing.NDArray) -> NumpyRounds:
        return []

    def _generate_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        return self._generate_typed_rounds(initial_groupings)

    def _init_participant_label_map(self, initial_groupings: np.typing.NDArray):
        def get_columns(i):
            start_index = sum(self.group_spec[0:i])
            end_index = start_index + self.group_spec[i]

            return initial_groupings[:, start_index:end_index].flatten().tolist()

        self._participant_types = [
            get_columns(i) for i in range(len(self.group_spec))
        ]

        if self._participant_labels is not None:
            self._participant_label_map = {
                p: self._participant_labels[i][j]
                for i, t in enumerate(self._participant_types)
                for j, p in enumerate(t)
            }
        else:
            self._participant_label_map = None
