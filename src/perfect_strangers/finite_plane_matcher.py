# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.design_types import DesignType, RTDType
from perfect_strangers.types import NumpyRounds, ParticipantLabels
from perfect_strangers.util import finite_field_elements, least_prime_factor, submatrix_transpositions


def _select_finite_plane_order(groups_per_round: int, group_size: int) -> int | None:
    if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
        return groups_per_round
    elif galois.is_prime_power(groups_per_round - 1) and group_size <= groups_per_round - 2:
        return groups_per_round - 1

    return None

def use_finite_plane_construction(groups_per_round: int, group_size: int) -> bool:
    plane_order = _select_finite_plane_order(groups_per_round, group_size)
    plane_order_test = plane_order is not None

    lpf = least_prime_factor(groups_per_round)
    group_size_lower_bound = lpf is not None and group_size > lpf

    return plane_order_test and group_size_lower_bound

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

class FinitePlaneMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int, plane_order: int, participant_labels: ParticipantLabels=None):
        self._used_verticals = False
        self._plane_order = plane_order
        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _generate_rounds_from_parallel_classes_of_plane(self):
        participants = self._group_matrices[0].copy()
        self._group_matrices = _match_on_finite_plane(participants)

        # Apply submatrix transposition.
        # For square matrices, transposition is equivalent to using the vertical lines of the finite plane.
        transpositions = submatrix_transpositions(participants)

        self._used_verticals = len(transpositions) > 0

        for t, s in transpositions:
            self._group_matrices += _match_on_finite_plane(t, s)

    def _generate_rounds_from_plane_one_order_smaller(self):
        self._used_verticals = True
        labels = np.arange(self._plane_order * (self.group_size + 1)).reshape(self.group_size + 1, self._plane_order)
        field_elements, _ = finite_field_elements(self._plane_order)

        rounds = [
            labels[0:self.group_size, :].transpose().tolist() + [labels[self.group_size, 0:self.group_size].tolist()]
        ]

        missing_row = 0

        for m in field_elements[1:self.group_size + 1]:
            xs = set(range(self.group_size + 1)) - {missing_row}
            cs_for_final_row = [y - m * field_elements[self.group_size] for y in field_elements[0:self.group_size]]

            new_round = [
                [labels[x, m * field_elements[x] + c] for x in xs]
                for c in cs_for_final_row
            ] + [
                [labels[x, m * field_elements[x] + c] for x in range(self.group_size)]
                for c in field_elements if c not in cs_for_final_row
            ] + [
                [labels[missing_row, m * missing_row + c] for c in cs_for_final_row]
            ]

            rounds.append(new_round)

            missing_row = (missing_row + 1) % self.group_size

        self._group_matrices = [np.array(r) for r in rounds]

    def _generate_rounds(self):
        if self._plane_order == self.groups_per_round:
            self._generate_rounds_from_parallel_classes_of_plane()
        elif self._plane_order == self.groups_per_round - 1:
            self._generate_rounds_from_plane_one_order_smaller()

    def _design_type(self) -> DesignType | None:
        if not self._used_verticals:
            return RTDType(self.group_size, self.groups_per_round)


        return None

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        plane_order = _select_finite_plane_order(groups_per_round, group_size)

        if plane_order is not None:
            return cls(groups_per_round, group_size, plane_order, participant_labels)

        return None

