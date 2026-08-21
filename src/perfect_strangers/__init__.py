# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Sequence

from perfect_strangers.__about__ import __version__
from perfect_strangers.factory import matcher_factory, typed_matcher_factory
from perfect_strangers.matchers import BaseMatcher, TypedMatcher
from perfect_strangers.types import GroupSpec

__all__ = ("__version__", "create_matcher", "create_typed_matcher")


def create_matcher(groups_per_round: int,
                   group_size: int,
                   participant_labels: Sequence | None=None) -> BaseMatcher:
    """
    Create a perfect stranger matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.

    :param group_size: The number of participants in each group.

    :param participant_labels: Unique labels for the experiment participants. This should be a sequence of participant
    labels with `groups_per_round * group_spec` unique elements.

    :return: A matcher object of a type which inherits from [`BaseMatcher`][perfect_strangers.BaseMatcher].
    """
    return matcher_factory(groups_per_round, group_size, participant_labels=participant_labels)

def create_typed_matcher(groups_per_round: int,
                         group_spec: GroupSpec,
                         participant_labels: Sequence | None=None) -> TypedMatcher:
    """
    Create a typed perfect stranger matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.

    :param group_spec: A sequence of integers specifying the composition of each group. The length of the provided sequence
    defines the number of different types of participant. The values in the sequence give the number of participants of each
    type in each group. The total number of participants per groups is given by the sum of the values in the sequence.

    :param participant_labels: Unique labels for the experiment participants. Either a sequence of labels, or a sequence of
    sequences of labels.

      * If a sequence of labels is provided it should contain as many unique labels as there are total participants in the
      experiment (i.e. `groups_per_round * sum(group_spec)`). These labels will be assigned to different participant types
      automatically.
      * To specify participant typings yourself, provide a sequence of sequences. There should be as many sequences as there
      are participant types (i.e. elements of `group_spec`). The n^th^ sequence should have `groups_per_round *
      group_spec[n]` unique elements.

    :return: A matcher object of a type which inherits from [`TypedMatcher`][perfect_strangers.TypedMatcher].
    """
    return typed_matcher_factory(groups_per_round, group_spec, participant_labels=participant_labels)
