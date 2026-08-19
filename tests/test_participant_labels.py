# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher, create_typed_matcher
from perfect_strangers.exceptions import IncorrectParticipantLabelsError, NonUniqueParticipantLabelsError
from perfect_strangers.util import unique_integers_summing_to_n


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 14))
def test_participant_labels(groups_per_round, group_size):
    participant_labels = [i + 10 for i in range(groups_per_round * group_size)]
    matcher = create_matcher(groups_per_round, group_size, participant_labels=participant_labels)
    groups = matcher.groups_for_next_round()

    assert {label for row in groups for label in row} == set(participant_labels)

    insufficient_labels = participant_labels[0:-2]

    with pytest.raises(IncorrectParticipantLabelsError):
        matcher = create_matcher(groups_per_round, group_size, insufficient_labels)

    non_unique_labels = participant_labels
    non_unique_labels[0] = non_unique_labels[1]

    with pytest.raises(NonUniqueParticipantLabelsError):
        matcher = create_matcher(groups_per_round, group_size, non_unique_labels)

group_specs = [
    spec
    for group_size in range(2, 7)
    for spec in unique_integers_summing_to_n(group_size)
]

@pytest.mark.parametrize("group_spec", group_specs)
@pytest.mark.parametrize("groups_per_round", range(2, 14))
def test_typed_participant_labels(groups_per_round, group_spec):
    offset = 10
    participant_labels = []

    for group_size in group_spec:
        type_labels = [i + offset for i in range(groups_per_round * group_size)]
        participant_labels.append(type_labels)
        offset += len(type_labels)

    matcher = create_typed_matcher(groups_per_round, group_spec, participant_labels=participant_labels)

    assert matcher.participant_types == participant_labels

    # Check typed matching respects specified typings.
    for r in matcher.rounds:
        for g in r:
            for i, n in enumerate(group_spec):
                assert len(set(g) & set(participant_labels[i])) == n

    with pytest.raises(ValueError, match=r"Participant labels should be a sequence of sequences."):
        matcher = create_typed_matcher(groups_per_round, group_spec, participant_labels=range(len(group_spec)))

    insufficient_labels = participant_labels.copy()
    insufficient_labels[0] = insufficient_labels[0][0:-1]

    with pytest.raises(IncorrectParticipantLabelsError):
        matcher = create_typed_matcher(groups_per_round, group_spec, participant_labels=insufficient_labels)

    non_unique_labels = participant_labels.copy()
    non_unique_labels[0][0] = non_unique_labels[0][1]

    with pytest.raises(NonUniqueParticipantLabelsError):
        matcher = create_typed_matcher(groups_per_round, group_spec, participant_labels=non_unique_labels)

@pytest.mark.parametrize("group_spec", group_specs)
@pytest.mark.parametrize("groups_per_round", range(2, 14))
def test_auto_typed_labels(groups_per_round, group_spec):
    offset = 10
    participant_labels = []

    for group_size in group_spec:
        type_labels = [i + offset for i in range(groups_per_round * group_size)]
        participant_labels.extend(type_labels)
        offset += len(type_labels)

    matcher = create_typed_matcher(groups_per_round, group_spec, participant_labels=participant_labels)

    # Check typed matching respects returned typings.
    for r in matcher.rounds:
        for g in r:
            for i, n in enumerate(group_spec):
                assert len(set(g) & set(matcher.participant_types[i])) == n
