# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Sequence

from perfect_strangers.exceptions import IncorrectParticipantLabelsError, NonUniqueParticipantLabelsError
from perfect_strangers.matchers import (
    BaseMatcher,
    ColumnShiftMatcher,
    FinitePlaneMatcher,
    KirkmanTripleMatcher,
    LookupMatcher,
    NearlyKirkmanTripleMatcher,
    RoundRobinMatcher,
    SubBIBDMatcher,
    TypedMatcher,
)
from perfect_strangers.types import GroupSpec
from perfect_strangers.util import use_finite_plane_construction


def _validate_matcher_spec(groups_per_round: int, group_size: int, participant_labels: Sequence | None):
    if participant_labels is not None:
        n_participants = groups_per_round * group_size
        n_labels = len(participant_labels)

        if n_labels != n_participants:
            raise IncorrectParticipantLabelsError(n_participants, n_labels)

        if len(set(participant_labels)) != n_participants:
            raise NonUniqueParticipantLabelsError(n_participants, len(set(participant_labels)))


def matcher_factory(groups_per_round: int,
                         group_size: int,
                         tried_sub_bibds: list[tuple[int, int]] | None=None,
                         participant_labels: Sequence | None=None) -> BaseMatcher:
    _validate_matcher_spec(groups_per_round, group_size, participant_labels)

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
    participant_labels_list = [participant_labels] if participant_labels is not None else None

    if algo_matcher is None and use_finite_plane_construction(groups_per_round, [group_size]):
        algo_matcher = FinitePlaneMatcher.create_matcher(groups_per_round,
                                                         [group_size],
                                                         participant_labels=participant_labels_list)

    # Try Theorem 4 from Ray-Chaudhuri and Wilson (1971).
    if algo_matcher is None and (groups_per_round, group_size) not in tried_sub_bibds:
        tried_sub_bibds.append((groups_per_round, group_size))
        algo_matcher = SubBIBDMatcher.create_matcher(groups_per_round,
                                                     group_size,
                                                     tried_sub_bibds,
                                                     participant_labels=participant_labels)

    # Default to column shift matching.
    if algo_matcher is None:
        algo_matcher = ColumnShiftMatcher(groups_per_round, [group_size], participant_labels=participant_labels_list)

    # If predefined sequences perform better use those.
    if lookup_matcher is not None and lookup_matcher.max_rounds > algo_matcher.max_rounds:
        return lookup_matcher

    return algo_matcher

def _validate_typed_matcher_spec(groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None):
    pass

def typed_matcher_factory(groups_per_round: int,
                           group_spec: GroupSpec,
                           participant_labels: Sequence[Sequence] | None) -> TypedMatcher:
    _validate_typed_matcher_spec(groups_per_round, group_spec, participant_labels)

    if use_finite_plane_construction(groups_per_round, group_spec):
        return FinitePlaneMatcher.create_matcher(groups_per_round, group_spec, participant_labels=participant_labels)


    return ColumnShiftMatcher(groups_per_round, group_spec, participant_labels=participant_labels)
