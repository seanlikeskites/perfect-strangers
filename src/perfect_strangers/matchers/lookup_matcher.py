# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json
from typing import TYPE_CHECKING

from perfect_strangers.matchers.base_matcher import BaseMatcher

if TYPE_CHECKING:
    from collections.abc import Sequence

    from perfect_strangers.types import RoundSequence


class LookupMatcher(BaseMatcher):
    """
    Fallback class to use the search results published by Both et al. (2016) - https://doi.org/10.1016/j.econlet.2016.06.028/
    """
    def __init__(self, round_sequence: RoundSequence, participant_labels: Sequence | None=None):
        super().__init__(round_sequence=round_sequence, participant_labels=participant_labels)

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: Sequence | None=None):
        with importlib.resources.files("perfect_strangers").joinpath("data/both_et_al_groupings.json").open() as f:
            grouping_data = json.loads(f.read())

        try:
            return cls(grouping_data[str(groups_per_round)][str(group_size)], participant_labels)
        except KeyError:
            return None
