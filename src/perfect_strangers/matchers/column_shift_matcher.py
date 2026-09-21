# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

import math
from typing import TYPE_CHECKING

import galois
import numpy as np

from perfect_strangers.matchers.transversal_matcher import TransversalMatcher
from perfect_strangers.util import least_prime_factor

if TYPE_CHECKING:
    from collections.abc import Sequence

    from perfect_strangers.types import GroupSpec, NumpyRounds


def _apply_sequential_shifts(base_matrix: np.typing.NDArray, n_shifts: int) -> NumpyRounds:
    shifts = []
    group_size = base_matrix.shape[1]

    for _ in range(n_shifts):
        for c in range(1, group_size):
            base_matrix[:, c] = np.roll(base_matrix[:, c], c)

        shifts.append(base_matrix.copy())

    return shifts

def _shift_columns(base_matrix: np.typing.NDArray) -> NumpyRounds:
    g = base_matrix.copy()
    groups_per_round = g.shape[0]
    group_size = g.shape[1]

    if groups_per_round < group_size:
        return []

    lpf = least_prime_factor(groups_per_round) or 0

    # If all column indices are coprime with groups_per_round
    # we can apply the maximum number of shifts.
    if group_size <= lpf:
        return _apply_sequential_shifts(g, groups_per_round - 1)

    # If no other strategy has worked, apply shifts until the rightmost column
    # with an index not coprime with groups_per_round would cycle round.
    non_cycle_column_index = group_size - 1

    while non_cycle_column_index > 0:
        if not galois.are_coprime(non_cycle_column_index, groups_per_round):
            break

        non_cycle_column_index -= 1

    n_shifts = math.ceil(groups_per_round / non_cycle_column_index) - 1

    return _apply_sequential_shifts(g, n_shifts)

class ColumnShiftMatcher(TransversalMatcher):
    def __init__(self, groups_per_round: int, group_spec: GroupSpec, participant_labels: Sequence | None=None):
        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _generate_typed_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        rounds = [initial_groupings]

        # Apply initial column shifts.
        rounds += _shift_columns(initial_groupings)

        return rounds
