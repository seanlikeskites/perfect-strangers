# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.finite_plane_matcher import FinitePlaneMatcher, use_finite_plane_construction
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.lookup_matcher import LookupMatcher
from perfect_strangers.nearly_kirkman_triple_matcher import NearlyKirkmanTripleMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher
from perfect_strangers.sub_bibd_matcher import SubBIBDMatcher


def matcher_factory(groups_per_round: int,
                    group_size: int,
                    tried_sub_bibds: list[tuple[int, int]] | None=None,
                    participant_labels: ParticipantLabels=None) -> BaseMatcher:
    """
    Create a groups matcher for the given experiment parameters.

    :param groups_per_round: The number of groups per round of the experiment.
    :param group_size: The number of participants in each group.
    :param participant_labels: A list of unique labels for the experiment participants. Must have `groups_per_round *
    group_size` unique elements.

    :return: A matcher object of a type which inherits from [`BaseMatcher`][perfect_strangers.BaseMatcher].
    """
    if tried_sub_bibds is None:
        tried_sub_bibds = []

    lookup_matcher = LookupMatcher.create_matcher(groups_per_round, group_size, participant_labels=participant_labels)
    algo_matcher: BaseMatcher | None = None

    # Try algorithms for specified group sizes.
    if group_size == 2:
        algo_matcher = RoundRobinMatcher(groups_per_round, participant_labels=participant_labels)
    elif group_size == 3:
        if groups_per_round % 2:
            algo_matcher = KirkmanTripleMatcher.create_matcher(groups_per_round, participant_labels=participant_labels)
        else:
            algo_matcher = NearlyKirkmanTripleMatcher.create_matcher(groups_per_round, participant_labels=participant_labels)

    # Try finite plane construction.
    if algo_matcher is None and use_finite_plane_construction(groups_per_round, group_size):
        algo_matcher = FinitePlaneMatcher.create_matcher(groups_per_round, group_size, participant_labels=participant_labels)

    # Try Theorem 4 from Ray-Chaudhuri and Wilson (1971).
    if algo_matcher is None and (groups_per_round, group_size) not in tried_sub_bibds:
        tried_sub_bibds.append((groups_per_round, group_size))
        algo_matcher = SubBIBDMatcher.create_matcher(groups_per_round,
                                                     group_size,
                                                     tried_sub_bibds,
                                                     participant_labels=participant_labels)

    # Default to column shift matching.
    if algo_matcher is None:
        algo_matcher = ColumnShiftMatcher(groups_per_round, group_size, participant_labels=participant_labels)

    # If predefined sequences perform better use those.
    if lookup_matcher is not None and lookup_matcher.max_rounds > algo_matcher.max_rounds:
        return lookup_matcher

    return algo_matcher
