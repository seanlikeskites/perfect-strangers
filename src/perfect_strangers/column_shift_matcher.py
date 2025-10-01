# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import math

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher


def _least_prime_factor(n: int) -> int | None:
    if n < 2:
        return None

    if n % 2 == 0:
        return 2

    f = 3

    while f <= math.sqrt(n):
        if n % f == 0:
            return f

        f += 2

    return n

def _shift_columns(base_matrix: np.typing.NDArray, stride: int) -> list[np.typing.NDArray]:
    g = base_matrix.copy()
    n_blocks = g.shape[0] // stride
    group_size = g.shape[1]

    if n_blocks < group_size:
        return []

    max_shifts = n_blocks - 1

    shifts = []
    column_positions = [0] * group_size
    column_history = np.zeros((n_blocks, group_size - 1))

    for _ in range(max_shifts):
        for c in range(1, group_size):
            g[:, c] = np.roll(g[:, c], c * stride)
            column_positions[c] = (column_positions[c] + c) % n_blocks

        for c in range(1, group_size):
            if column_history[column_positions[c], c - 1] != 0:
                break
        else:
            for c in range(1, group_size):
                column_history[column_positions[c], c - 1] = 1

            if len(set(column_positions)) == group_size:
                shifts.append(g.copy())

    return shifts

class ColumnShiftMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int):
        super().__init__(groups_per_round, group_size)

    def _generate_rounds(self):
        # Apply initial column shifts.
        self.group_matrices += _shift_columns(self.group_matrices[0], 1)

        # Apply submatrix transposition.
        block_size = self.groups_per_round
        n_blocks = 1

        while block_size % self.group_size == 0:
            g = self.group_matrices[0].copy()

            stride = block_size // self.group_size

            for block in range(n_blocks):
                block_start = block * block_size

                for sub in range(stride):
                    start_col = block_start + sub
                    end_col = start_col + self.group_size * stride
                    g[start_col:end_col:stride, :] = g[start_col:end_col:stride, :].transpose()

            self.group_matrices.append(g)
            self.group_matrices += _shift_columns(g, block_size)

            block_size = stride
            n_blocks *= self.group_size

