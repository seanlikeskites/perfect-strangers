# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher

__all__ = ("__version__", "create_matcher")


def create_matcher(groups_per_round: int, group_size: int) -> BaseMatcher:
    """
    Create a groups matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.
    :param group_size: The number of participants in each group.

    :return: A matcher object of a type which inherits from [`BaseMatcher`][perfect_strangers.BaseMatcher].
    """
    if group_size == 2:
        return RoundRobinMatcher(groups_per_round)

    if group_size == 3:
        matcher = KirkmanTripleMatcher.create_matcher(groups_per_round)

        if matcher is not None:
            return matcher

    return ColumnShiftMatcher(groups_per_round, group_size)
