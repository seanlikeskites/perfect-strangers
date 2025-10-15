# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Callable

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, RoundSequence

ParameterFuncReturn = tuple[int, int] | None
RoundGenerator = Callable[[int, int], RoundSequence]

def _get_t_from_q(q: int) -> ParameterFuncReturn:
    if not galois.is_prime_power(q) or q % 6 != 1:
        return None

    t = (q - 1) // 6

    return t, q

def _three_q_params(groups_per_round: int) -> ParameterFuncReturn:
    return _get_t_from_q(groups_per_round)

def _two_q_less_one_params(groups_per_round: int) -> ParameterFuncReturn:
    if groups_per_round % 2 == 0:
        return None

    q = (3 * groups_per_round - 1) // 2

    return _get_t_from_q(q)

def _galois_field_elements(order: int) -> tuple[list[galois.FieldArray], galois.FieldArray]:
    gf = galois.GF(order)
    elements = [gf(i) for i in range(order)]
    primitive_element = gf.primitive_element

    return elements, primitive_element

def _three_q_rounds(t: int, q: int) -> RoundSequence:
    labels = np.arange(3 * q).reshape(q, 3)

    field_elements, g = _galois_field_elements(q)

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

def _two_q_less_one_rounds(t: int, q: int) -> RoundSequence:
    labels = np.arange(2 * q).reshape(q, 2)
    inf = 2 * q

    field_elements, g = _galois_field_elements(q)

    # Find m.
    target = (g ** t + galois.GF(q)(1)) / galois.GF(q)(2)
    m = target.log(g)

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
    def __init__(self, groups_per_round: int, t: int, q: int, round_generator: RoundGenerator):
        self.t = t
        self.q = q
        self.round_generator = round_generator

        super().__init__(groups_per_round, 3)

    def _generate_rounds(self):
        self.group_matrices = self.round_generator(self.t, self.q)

    @classmethod
    def create_matcher(cls, groups_per_round: int):
        methods = [
            (_three_q_params, _three_q_rounds),
            (_two_q_less_one_params, _two_q_less_one_rounds)
        ]

        for parameter_func, round_generator in methods:
            params = parameter_func(groups_per_round)

            if params is not None:
                t, q = params
                return KirkmanTripleMatcher(groups_per_round, t, q, round_generator)

        return None
