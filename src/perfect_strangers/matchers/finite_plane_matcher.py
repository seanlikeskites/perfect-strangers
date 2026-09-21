# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import galois
import numpy as np

from perfect_strangers.matchers.transversal_matcher import TransversalMatcher
from perfect_strangers.types import GroupSpec, NumpyRounds
from perfect_strangers.util import finite_field_elements, group_size_from_spec


def _match_on_finite_plane(participants: np.typing.NDArray) -> NumpyRounds:
    groups_per_round = participants.shape[0]
    group_size = participants.shape[1]

    if groups_per_round < group_size:
        return [participants]

    labels = participants.transpose()
    field_elements, _ = finite_field_elements(groups_per_round)

    rounds = []

    for m in field_elements:
        new_round = [
            [labels[x, m * field_elements[x] + c] for x in range(group_size)]
            for c in field_elements
        ]

        rounds.append(new_round)

    return [np.array(r) for r in rounds]

class FinitePlaneMatcher(TransversalMatcher):
    def __init__(self, groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None=None):
        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _generate_typed_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        participants = initial_groupings.copy()
        return _match_on_finite_plane(participants)

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None=None):
        group_size = group_size_from_spec(group_spec)

        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return cls(groups_per_round, group_spec, participant_labels)

        return None
