# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.lookup_matcher import LookupMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher

__all__ = ("__version__", "create_matcher")


def create_matcher(groups_per_round: int, group_size: int) -> BaseMatcher:
    """
    Create a groups matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.
    :param group_size: The number of participants in each group.

    :return: A matcher object of a type which inherits from [`BaseMatcher`][perfect_strangers.BaseMatcher].
    """
    lookup_matcher = LookupMatcher.create_matcher(groups_per_round, group_size)
    algo_matcher = None

    if group_size == 2:
        algo_matcher = RoundRobinMatcher(groups_per_round)
    elif group_size == 3:
        matcher = KirkmanTripleMatcher.create_matcher(groups_per_round)

        if matcher is not None:
            algo_matcher = matcher

    if algo_matcher is None:
        algo_matcher = ColumnShiftMatcher(groups_per_round, group_size)

    if lookup_matcher is not None and lookup_matcher.max_rounds > algo_matcher.max_rounds:
        return lookup_matcher

    return algo_matcher
