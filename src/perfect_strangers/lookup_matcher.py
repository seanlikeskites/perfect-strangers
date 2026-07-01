# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher


class LookupMatcher(BaseMatcher):
    """
    Fallback class to use the search results published by Both et al. (2016) - https://doi.org/10.1016/j.econlet.2016.06.028/
    """
    def __init__(self, rounds: list[list[list[int]]]):
        groups_per_round = len(rounds[0])
        group_size = len(rounds[0][0])

        super().__init__(groups_per_round, group_size)

        self.group_matrices = [np.array(g) for g in rounds]

    def _generate_rounds(self):
        pass

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int):
        with importlib.resources.files("perfect_strangers").joinpath("lookup/both_et_al_groupings.json").open() as f:
            grouping_data = json.loads(f.read())

        try:
            return LookupMatcher(grouping_data[str(groups_per_round)][str(group_size)])
        except KeyError:
            return None
