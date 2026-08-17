# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import galois
import numpy as np

from perfect_strangers.design_types import DesignType, RTDType
from perfect_strangers.matchers.typed_matcher import TypedMatcher
from perfect_strangers.types import GroupSpec, NumpyRounds
from perfect_strangers.util import (
    finite_field_elements,
    group_size_from_spec,
    submatrix_transpositions,
)


def _match_on_finite_plane(participants: np.typing.NDArray, stride: int=1) -> NumpyRounds:
    n_blocks = participants.shape[0] // stride
    group_size = participants.shape[1]

    if n_blocks < group_size:
        return [participants]

    labels = [participants[b::stride, :].transpose() for b in range(stride)]
    field_elements, _ = finite_field_elements(n_blocks)

    rounds = []

    for m in field_elements:
        new_round = [
            [l[x, m * field_elements[x] + c] for x in range(l.shape[0])]
            for c in field_elements
            for l in labels
        ]

        rounds.append(new_round)

    return [np.array(r) for r in rounds]

class FinitePlaneMatcher(TypedMatcher):
    def __init__(self, groups_per_round: int, group_spec: GroupSpec | int, participant_labels: Sequence | None=None):
        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _generate_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        participants = initial_groupings.copy()
        rounds = _match_on_finite_plane(participants)

        # Apply submatrix transposition.
        # For square matrices, transposition is equivalent to using the vertical lines of the finite plane.
        transpositions = submatrix_transpositions(participants)

        self._performed_transposition = len(transpositions) > 0

        for t, s in transpositions:
            rounds += _match_on_finite_plane(t, s)

        return rounds

    def _design_type(self) -> DesignType | None:
        if not self._performed_transposition:
            return RTDType(self.group_size, self.groups_per_round)

        return None

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_spec: GroupSpec | int, participant_labels: Sequence | None=None):
        group_size = group_size_from_spec(group_spec)

        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return cls(groups_per_round, group_spec, participant_labels)

        return None
