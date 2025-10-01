# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher

__all__ = ("__version__", "create_matcher")


def create_matcher(groups_per_round: int, group_size: int):
    if group_size == 2:
        return RoundRobinMatcher(groups_per_round)

    return ColumnShiftMatcher(groups_per_round, group_size)
