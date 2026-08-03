# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import math
from typing import TYPE_CHECKING

import galois

if TYPE_CHECKING:
    import numpy.typing as npt

    from perfect_strangers.types import GroupingMatrix


def sequence_length_upper_bound(groups_per_round: int, group_size: int) -> int:
    if groups_per_round < group_size:
        return 1

    # (3, 1)-RGGD of type 2^6 does not exist.
    if groups_per_round == 4 and group_size == 3:
        return 4

    return (groups_per_round * group_size - 1) // (group_size - 1)

def is_round_valid(g: npt.NDArray, groups_per_round: int, group_size: int) -> bool:
    n_groups_check = g.shape[0] == groups_per_round
    group_size_check = g.shape[1] == group_size
    participants_check = set(g.flatten()) == set(range(g.size))

    return n_groups_check and group_size_check and participants_check

def is_round_pair_valid(r1: npt.NDArray, r2: npt.NDArray) -> bool:
    for i in range(r1.shape[0]):
        g1 = set(r1[i, :])

        for j in range(r2.shape[0]):
            g2 = set(r2[j, :])

            if len(g1 & g2) > 1:
                return False

    return True

def least_prime_factor(n: int) -> int | None:
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

def x_is_power_of_y(x: int, y: int) -> bool:
    while x % y == 0:
        x //= y

    return x == 1

def finite_field_elements(order: int) -> tuple[list[galois.FieldArray], galois.FieldArray]:
    gf = galois.GF(order)
    elements = [gf(i) for i in range(order)]
    primitive_element = gf.primitive_element

    return elements, primitive_element

def submatrix_transpositions(matrix: npt.NDArray):
    matrix = matrix.copy()
    transposed = False

    if matrix.shape[1] > matrix.shape[0]:
        matrix = matrix.transpose()
        transposed = True

    block_size = matrix.shape[1]

    transpositions = []

    while matrix.shape[0] % block_size == 0:
        m = matrix.copy()

        stride = block_size // matrix.shape[1]
        n_blocks = matrix.shape[0] // block_size

        for block in range(n_blocks):
            block_start = block * block_size

            for sub in range(stride):
                start_row = block_start + sub
                end_row = start_row + matrix.shape[1] * stride
                m[start_row:end_row:stride, :] = m[start_row:end_row:stride, :].transpose()

        transpositions.append((m, block_size))
        block_size *= matrix.shape[1]

    if transposed:
        transpositions = [(t[0].transpose(), b) for t, b in transpositions]

    return transpositions

def round_to_sets(r: GroupingMatrix):
    return {frozenset(g) for g in r}

def round_to_lists(r: GroupingMatrix):
    return [list(g) for g in r]
