# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.round_robin_matcher import RoundRobinMatcher

__all__ = ("__version__", "create_matcher")


def create_matcher(groups_per_round, group_size):
    if group_size == 2:
        return RoundRobinMatcher(groups_per_round)

    return None
