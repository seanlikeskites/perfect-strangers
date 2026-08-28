# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json
from typing import TYPE_CHECKING

import numpy as np

from perfect_strangers.matchers.typed_matcher import TypedMatcher
from perfect_strangers.util import group_size_from_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

    from perfect_strangers.types import GroupSpec, NumpyRounds


class RTDMatcher(TypedMatcher):
    """
    Class to construct an RTD(k, n) from k - 1 MOLS of order N.
    """
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 mols: list[np.typing.NDArray],
                 participant_labels: Sequence | None=None):
        self._mols = mols
        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _construct_parallel_class(self,
                                  block_squares: list[np.typing.NDArray],
                                  class_square: np.typing.NDArray,
                                  design_groups: np.typing.NDArray,
                                  class_index: int) -> np.typing.NDArray:
        p = np.empty((self.groups_per_round, self.group_size), dtype=int)

        for i in range(self.groups_per_round):
            j = list(class_square[i]).index(class_index)

            p[i, 0] = design_groups[i, 0]
            p[i, 1] = design_groups[j, 1]

            for k in range(2, self.group_size):
                s = block_squares[k - 2]
                p[i, k] = design_groups[s[i, j], k]

        return p

    def _generate_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        block_squares = self._mols[0:self.group_size - 1]
        class_square = self._mols[-1]

        return [
            self._construct_parallel_class(block_squares,
                                           class_square,
                                           initial_groupings,
                                           i)
            for i in range(self.groups_per_round)
        ]

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None=None):
        group_size = group_size_from_spec(group_spec)

        if group_size < 3:
            return None

        with importlib.resources.files("perfect_strangers").joinpath("data/mols.json").open() as f:
            data = json.loads(f.read())

        try:
            mols = data[str(groups_per_round)]["matrices"]

        except KeyError:
            return None

        if len(mols) >= group_size - 1:
            return cls(groups_per_round,
                       group_spec,
                       [np.array(m) for m in mols],
                       participant_labels=participant_labels)

        return None
