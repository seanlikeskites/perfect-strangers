# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import numpy as np
import galois

from perfect_strangers.base_matcher import BaseMatcher
from perfect_strangers.util import primitive_root_mod_n, root_of_prime_power


def _t_parameter(q: int) -> int | None:
    if q % 6 != 1:
        return None

    return (q - 1) // 6

def _first_method_kirkman_parameters(groups_per_round: int) -> tuple[int, int, int, int] | None:
    if root_of_prime_power(groups_per_round) is None:
        return None

    t = _t_parameter(groups_per_round)

    if t is None:
        return None

    return t, groups_per_round, groups_per_round, 0

def _second_method_kirkman_parameters(groups_per_round: int) -> tuple[int, int, int, int] | None:
    if groups_per_round % 2 == 0:
        return None

    q = (3 * groups_per_round - 1) // 2

    if root_of_prime_power(q) is None:
        return None

    t = _t_parameter(q)

    if t is None:
        return None

    return t, q, groups_per_round, 1

def get_kirkman_parameters(groups_per_round: int) -> tuple[int, int, int, int] | None:
    params = _first_method_kirkman_parameters(groups_per_round)

    if params is not None:
        return params

    return _second_method_kirkman_parameters(groups_per_round)

def _first_method(t: int, q: int, g: galois.FieldArray):
    labels = np.arange(3 * q).reshape(q, 3)

    field_elements = [galois.GF(q)(i) for i in range(q)]

    rounds = []

    for shift in field_elements:
        new_groups = np.empty((q, 3))

        new_groups[0, :] = labels[shift, :]

        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_groups[group_idx, :] = [
                    labels[(shift + g ** i), j],
                    labels[(shift + g ** (i + 2 * t)), j],
                    labels[(shift + g ** (i + 4 * t)), j],
                ]

                group_idx += 1

        for i in range(6 * t):
            if (i // t) % 2 == 0:
                continue

            new_groups[group_idx, :] = [
                labels[(shift + g ** i), 0],
                labels[(shift + g ** (i + 2 * t)), 1],
                labels[(shift + g ** (i + 4 * t)), 2],
            ]

            group_idx += 1

        rounds.append(new_groups)

    for i in range(6 * t):
        if (i // t) % 2 != 0:
            continue

        new_groups = np.empty((q, 3))

        for shift in field_elements:
            new_groups[shift, :] = [
                labels[(shift + g ** i), 0],
                labels[(shift + g ** (i + 2 * t)), 1],
                labels[(shift + g ** (i + 4 * t)), 2],
            ]

        rounds.append(new_groups)

    return rounds

def _second_method(t: int, q: int, g: galois.FieldArray):
    labels = np.arange(2 * q).reshape(q, 2)
    inf = 2 * q

    # Find m.
    target = (g ** t + galois.GF(q)(1)) / galois.GF(q)(2)
    m = target.log(g)

    field_elements = [galois.GF(q)(i) for i in range(q)]

    rounds = []

    for shift in field_elements:
        new_groups = np.empty(((2 * q + 1) // 3, 3))

        new_groups[0, :] = [
            labels[shift, 0],
            labels[shift, 1],
            inf
        ]

        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_groups[group_idx, :] = [
                    labels[(shift + g ** (i + 2 * j * t)), 0],
                    labels[(shift + g ** (i + 2 * j * t + t)), 0],
                    labels[(shift + g ** (i + 2 * j * t + m)), 1]
                ]

                group_idx += 1

            new_groups[group_idx, :] = [
                labels[(shift + g ** (i + m + t)), 1],
                labels[(shift + g ** (i + m + 3 * t)), 1],
                labels[(shift + g ** (i + m + 5 * t)), 1]
            ]

            group_idx += 1

        rounds.append(new_groups)

    return rounds

class KirkmanTripleMatcher(BaseMatcher):
    """ Implementation as per https://math.stackexchange.com/a/4510645"""
    def __init__(self, params: tuple[int, int, int, int]):
        self.t, self.q, _, self.method = params
        super().__init__(params[2], 3)

    def _generate_rounds(self):
        g = galois.GF(self.q).primitive_element

        if self.method == 0:
            self.group_matrices = _first_method(self.t, self.q, g)
        else:
            self.group_matrices = _second_method(self.t, self.q, g)

    @classmethod
    def create_matcher(cls, groups_per_round: int):
        if (kirkman_params := get_kirkman_parameters(groups_per_round)) is not None:
            return KirkmanTripleMatcher(kirkman_params)
        else:
            return None
