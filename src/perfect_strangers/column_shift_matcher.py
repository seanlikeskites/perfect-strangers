# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import math

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.util import least_prime_factor


def _shift_columns(base_matrix: np.typing.NDArray, stride: int) -> list[np.typing.NDArray]:
    g = base_matrix.copy()
    n_blocks = g.shape[0] // stride
    group_size = g.shape[1]

    if n_blocks < group_size:
        return []

    lpf = least_prime_factor(n_blocks)

    if group_size <= lpf:
        n_shifts = n_blocks - 1
    else:
        # In some cases we can get away with more shifts. Need to work out a good
        # way of calculating this.
        n_shifts = math.ceil(n_blocks / (group_size - 1)) - 1

    shifts = []

    for _ in range(n_shifts):
        for c in range(1, group_size):
            g[:, c] = np.roll(g[:, c], c * stride)

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

