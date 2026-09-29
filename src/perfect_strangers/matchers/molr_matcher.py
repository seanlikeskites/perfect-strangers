# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json
from typing import TYPE_CHECKING

import numpy as np

from perfect_strangers.matchers.transversal_matcher import TransversalMatcher
from perfect_strangers.util import group_size_from_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

    from perfect_strangers.types import GroupSpec, NumpyRounds


def _round_from_latin_rectangle(initial_groupings: np.typing.NDArray, rect: np.typing.NDArray):
    groups_per_round = initial_groupings.shape[0]
    group_size = initial_groupings.shape[1]

    new_round = np.empty((groups_per_round, group_size), dtype="int")

    for g in range(groups_per_round):
        for p in range(group_size):
            new_round[rect[g, p], p] = initial_groupings[g, p]

    return new_round


class MOLRMatcher(TransversalMatcher):
    """
    Construct rounds from a set of MOLRs.
    """
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 molr: list[np.typing.NDArray],
                 participant_labels: Sequence | None=None):
        self._molr = molr
        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _generate_typed_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        rounds = [initial_groupings]

        rounds.extend(
            [_round_from_latin_rectangle(initial_groupings, rect) for rect in self._molr]
        )

        return rounds

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None=None):
        group_size = group_size_from_spec(group_spec)

        with importlib.resources.files("perfect_strangers").joinpath("data/molr.json").open() as f:
            data = json.loads(f.read())

        try:
            candidate_molr = data[str(groups_per_round)]

        except KeyError:
            return None

        if candidate_molr["n_cols"] >= group_size:
            molr = candidate_molr["matrices"]
            return cls(groups_per_round,
                       group_spec,
                       [np.array(n) for n in molr],
                       participant_labels=participant_labels)

        return None
