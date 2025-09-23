# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import math

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher


def _least_prime_factor(n):
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


class ColumnShiftMatcher(BaseMatcher):
    def __init__(self, groups_per_round, group_size):
        super().__init__(groups_per_round, group_size)

    def _generate_rounds(self):
        # Apply column shifts
        def _shift_columns(g):
            for c in range(1, g.shape[1]):
                g[:, c] = np.roll(g[:, c], c)

            return g

        lpf = _least_prime_factor(self.groups_per_round)

        if self.group_size <= lpf:
            n_shifts = self.groups_per_round - 1
        else:
            # In some cases we can get away with more shifts. Need to work out a good
            # way of calculating this.
            n_shifts = math.ceil(self.groups_per_round / (self.group_size - 1)) - 1

        for _ in range(n_shifts):
            self.group_matrices.append(_shift_columns(self.group_matrices[-1].copy()))

        # If possible apply a transpose.
        if self.groups_per_round % self.group_size == 0:
            g = self.group_matrices[0].copy()

            for sub in range(self.groups_per_round // self.group_size):
                start_col = sub * self.group_size
                end_col = start_col + self.group_size
                g[start_col:end_col, :] = g[start_col:end_col, :].transpose()

            self.group_matrices.append(g)

