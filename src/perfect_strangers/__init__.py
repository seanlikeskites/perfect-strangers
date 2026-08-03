# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.__about__ import __version__
from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.factory import matcher_factory
from perfect_strangers.types import ParticipantLabels

__all__ = ("__version__", "create_matcher")


def create_matcher(groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None) -> BaseMatcher:
    """
    Create a groups matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.
    :param group_size: The number of participants in each group.
    :param participant_labels: A list of unique labels for the experiment participants. Must have `groups_per_round *
    group_size` unique elements.

    :return: A matcher object of a type which inherits from [`BaseMatcher`][perfect_strangers.BaseMatcher].
    """
    return matcher_factory(groups_per_round, group_size, participant_labels=participant_labels)
