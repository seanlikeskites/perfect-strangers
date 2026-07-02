# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import math

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels, RoundSequence
from perfect_strangers.util import least_prime_factor, submatrix_transpositions


def _apply_sequential_shifts(base_matrix: np.typing.NDArray, n_shifts: int, stride: int) -> RoundSequence:
    shifts = []
    group_size = base_matrix.shape[1]

    for _ in range(n_shifts):
        for c in range(1, group_size):
            base_matrix[:, c] = np.roll(base_matrix[:, c], c * stride)

        shifts.append(base_matrix.copy())

    return shifts

def _shift_columns(base_matrix: np.typing.NDArray, stride: int) -> RoundSequence:
    g = base_matrix.copy()
    n_blocks = g.shape[0] // stride
    group_size = g.shape[1]

    if n_blocks < group_size:
        return []

    lpf = least_prime_factor(n_blocks) or 0

    # If all column indices are coprime with n_blocks we can apply the maximum
    # number of shifts.
    if group_size <= lpf:
        return _apply_sequential_shifts(g, n_blocks - 1, stride)

    # If no other strategy has worked, apply shifts until the rightmost column
    # with an index not coprime with n_blocks would cycle round.
    non_cycle_column_index = group_size - 1

    while non_cycle_column_index > 0:
        if not galois.are_coprime(non_cycle_column_index, n_blocks):
            break

        non_cycle_column_index -= 1

    n_shifts = math.ceil(n_blocks / non_cycle_column_index) - 1

    return _apply_sequential_shifts(g, n_shifts, stride)

class ColumnShiftMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels=None):
        super().__init__(groups_per_round, group_size, participant_labels)

    def _generate_rounds(self):
        # Apply initial column shifts.
        self._group_matrices += _shift_columns(self._group_matrices[0], 1)

        # Apply submatrix transposition.
        transpositions = submatrix_transpositions(self._group_matrices[0])

        for t, stride in transpositions:
            self._group_matrices.append(t)
            self._group_matrices += _shift_columns(t, stride)

