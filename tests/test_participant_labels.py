# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from perfect_strangers.base_matcher import IncorrectParticipantLabelsError, NonUniqueParticipantLabelsError


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 14))
def test_benchmarks(groups_per_round, group_size):
    participant_labels = [i + 10 for i in range(groups_per_round * group_size)]
    matcher = create_matcher(groups_per_round, group_size, participant_labels)
    groups = matcher.groups_for_next_round()

    assert {label for row in groups for label in row} == set(participant_labels)

    insufficient_labels = participant_labels[0:-2]

    with pytest.raises(IncorrectParticipantLabelsError):
        matcher = create_matcher(groups_per_round, group_size, insufficient_labels)

    non_unique_labels = participant_labels
    non_unique_labels[0] = non_unique_labels[1]

    with pytest.raises(NonUniqueParticipantLabelsError):
        matcher = create_matcher(groups_per_round, group_size, non_unique_labels)
