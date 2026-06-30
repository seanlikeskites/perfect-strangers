# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.lookup_matcher import LookupMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher
from perfect_strangers.rtd_matcher import RTDMatcher
from perfect_strangers.util import least_prime_factor

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

    # Try algorithms for specified group sizes.
    if group_size == 2:
        algo_matcher = RoundRobinMatcher(groups_per_round)
    elif group_size == 3:
        algo_matcher = KirkmanTripleMatcher.create_matcher(groups_per_round)

    # Try TRD construction.
    if groups_per_round >= 2 and group_size > least_prime_factor(groups_per_round):
        algo_matcher = RTDMatcher.create_matcher(groups_per_round, group_size)

    # Default to column shift matching.
    if algo_matcher is None:
        algo_matcher = ColumnShiftMatcher(groups_per_round, group_size)

    # If predefined sequences perform better use those.
    if lookup_matcher is not None and lookup_matcher.max_rounds > algo_matcher.max_rounds:
        return lookup_matcher

    return algo_matcher
