# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import numpy as np

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

def _first_method(t: int, q: int, g: int):
    labels = np.arange(3 * q).reshape(q, 3)

    rounds = []

    for shift in range(q):
        new_groups = np.empty((q, 3))

        new_groups[0, :] = labels[shift, :]

        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_groups[group_idx, :] = [
                    labels[(shift + g ** i) % q, j],
                    labels[(shift + g ** (i + 2 * t)) % q, j],
                    labels[(shift + g ** (i + 4 * t)) % q, j],
                ]

                group_idx += 1

        for i in range(6 * t):
            if (i // t) % 2 == 0:
                continue

            new_groups[group_idx, :] = [
                labels[(shift + g ** i) % q, 0],
                labels[(shift + g ** (i + 2 * t)) % q, 1],
                labels[(shift + g ** (i + 4 * t)) % q, 2],
            ]

            group_idx += 1

        rounds.append(new_groups)
        break

    for i in range(6 * t):
        if (i // t) % 2 != 0:
            continue

        new_groups = np.empty((q, 3))

        for shift in range(q):
            new_groups[shift, :] = [
                labels[(shift + g ** i) % q, 0],
                labels[(shift + g ** (i + 2 * t)) % q, 1],
                labels[(shift + g ** (i + 4 * t)) % q, 2],
            ]

        rounds.append(new_groups)

    return rounds

def _second_method(t: int, q: int, g: int):
    labels = np.arange(2 * q).reshape(q, 2)
    inf = 2 * q

    # Find m.
    target = (g ** t + 1) % q
    m = 2

    while (2 * g ** m) % q != target:
        m += 1

    rounds = []

    for shift in range(q):
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
                    labels[(shift + g ** (i + 2 * j * t)) % q, 0],
                    labels[(shift + g ** (i + 2 * j * t + t)) % q, 0],
                    labels[(shift + g ** (i + 2 * j * t + m)) % q, 1]
                ]

                group_idx += 1

            new_groups[group_idx, :] = [
                labels[(shift + g ** (i + m + t)) % q, 1],
                labels[(shift + g ** (i + m + 3 * t)) % q, 1],
                labels[(shift + g ** (i + m + 5 * t)) % q, 1]
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
        g = primitive_root_mod_n(self.q)

        if self.method == 0:
            self.group_matrices = _first_method(self.t, self.q, g)
        else:
            self.group_matrices = _second_method(self.t, self.q, g)
