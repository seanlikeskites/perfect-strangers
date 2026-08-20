# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from collections.abc import Callable, Sequence

import galois
import numpy as np

from perfect_strangers.design_types import DesignType, RBIBDType
from perfect_strangers.matchers.base_matcher import BaseMatcher
from perfect_strangers.types import NumpyRounds
from perfect_strangers.util import finite_field_elements

ParameterFuncReturn = tuple[int, int] | None
RoundGenerator = Callable[[int, int], NumpyRounds]

def _t_from_q(q: int, n: int) -> ParameterFuncReturn:
    """
    Check q is a prime power of the form nt + 1 and return t and q if it is.

    :return: Tuple of (t, q) if q is a prime power of the form nt + 1, None otherwise.
    """
    if not galois.is_prime_power(q) or q % n != 1:
        return None

    t = (q - 1) // n

    return t, q

#######################################################################
# Theorem 5 from Ray-Chaudhuri and Wilson (1971):
#   Where q = 6t + 1 is a prime power construct a Kirkman triple
#   system for 3q total participants.
#######################################################################
def _rw_theorem5_params(groups_per_round: int) -> ParameterFuncReturn:
    return _t_from_q(groups_per_round, 6)

def _rw_theorem5_rounds(t: int, q: int) -> NumpyRounds:
    labels = np.arange(3 * q).reshape(q, 3)
    field_elements, g = finite_field_elements(q)

    def next_group(shift, i, j=None):
        return [labels[shift + g ** (i + 2 * x * t), j if j is not None else x] for x in range(3)]

    rounds = []

    for shift in field_elements:
        new_round = np.empty((q, 3), dtype="int")
        new_round[0, :] = labels[shift, :]
        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_round[group_idx, :] = next_group(shift, i, j)
                group_idx += 1

        for i in range(6 * t):
            if (i // t) % 2 == 0:
                continue

            new_round[group_idx, :] = next_group(shift, i)
            group_idx += 1

        rounds.append(new_round)

    for i in range(6 * t):
        if (i // t) % 2 != 0:
            continue

        new_round = np.empty((q, 3), dtype="int")

        for shift in field_elements:
            new_round[shift, :] = next_group(shift, i)

        rounds.append(new_round)

    return rounds

#######################################################################
# Theorem 6 from Ray-Chaudhuri and Wilson (1971)
#   Where q = 6t + 1 is a prime power construct a Kirkman triple
#   system for 2q + 1 total participants.
#######################################################################
def _rw_theorem6_params(groups_per_round: int) -> ParameterFuncReturn:
    if groups_per_round % 2 == 0:
        return None

    q = (3 * groups_per_round - 1) // 2

    return _t_from_q(q, 6)

def _rw_theorem6_rounds(t: int, q: int) -> NumpyRounds:
    groups_per_round = (2 * q + 1) // 3
    labels = np.arange(2 * q).reshape(q, 2)
    inf = 2 * q

    field_elements, g = finite_field_elements(q)

    # Find m.
    target = (g ** t + field_elements[1]) / field_elements[2]
    m = target.log(g)

    rounds = []

    for shift in field_elements:
        new_round = np.empty((groups_per_round, 3), dtype="int")

        new_round[0, :] = [
            labels[shift, 0],
            labels[shift, 1],
            inf
        ]

        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_round[group_idx, :] = [
                    labels[shift + g ** (i + 2 * j * t), 0],
                    labels[shift + g ** (i + 2 * j * t + t), 0],
                    labels[shift + g ** (i + 2 * j * t + m), 1]
                ]

                group_idx += 1

            new_round[group_idx, :] = [
                labels[shift + g ** (i + m + t), 1],
                labels[shift + g ** (i + m + 3 * t), 1],
                labels[shift + g ** (i + m + 5 * t), 1]
            ]

            group_idx += 1

        rounds.append(new_round)

    return rounds

#######################################################################
# Lemma 3 from Hanani et. al. (1972):
#   Where q = 4t + 1 is a prime power construct a (3q + 1, 4, 1)-RBIBD.
#######################################################################
def _hrw_lemma3_params(groups_per_round: int) -> ParameterFuncReturn:
    if groups_per_round % 3 != 1:
        return None

    q = (4 * groups_per_round - 1) // 3

    return _t_from_q(q, 4)

def _hrw_lemma3_rounds(t: int, q: int) -> NumpyRounds:
    groups_per_round = (3 * q + 1) // 4
    labels = np.arange(3 * q).reshape(q, 3)
    inf = 3 * q

    field_elements, g = finite_field_elements(q)

    rounds = []

    for shift in field_elements:
        new_round = np.empty((groups_per_round, 4), dtype="int")

        new_round[0, :] = [
            labels[shift, 0],
            labels[shift, 1],
            labels[shift, 2],
            inf
        ]

        group_idx = 1

        for i in range(t):
            for j in range(3):
                new_round[group_idx, :] = [
                    labels[shift + g ** i, (0 + j) % 3],
                    labels[shift + g ** (i + 2 * t), (0 + j) % 3],
                    labels[shift + g ** (i + t), (1 + j) % 3],
                    labels[shift + g ** (i + 3 * t), (1 + j) % 3],
                ]

                group_idx += 1

        rounds.append(new_round)

    return rounds

#######################################################################
# Matcher
#######################################################################
class PrimitiveElementMatcher(BaseMatcher):
    def __init__(self,
                 groups_per_round: int,
                 group_size: int,
                 t: int,
                 q: int,
                 round_generator: RoundGenerator,
                 participant_labels: Sequence | None=None):
        self.t = t
        self.q = q
        self.round_generator = round_generator

        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _generate_rounds(self, _initial_groupings: np.typing.NDArray) -> NumpyRounds:
        return self.round_generator(self.t, self.q)

    def _design_type(self) -> DesignType:
        return RBIBDType(self.n_participants, self.group_size)

    @classmethod
    def create_matcher(cls,
                       groups_per_round: int,
                       group_size: int,
                       participant_labels: Sequence | None=None):
        methods = {
            3: [
                (_rw_theorem5_params, _rw_theorem5_rounds),
                (_rw_theorem6_params, _rw_theorem6_rounds)
            ],
            4: [
                (_hrw_lemma3_params, _hrw_lemma3_rounds)
            ]
        }

        if group_size not in methods:
            return None

        for parameter_func, round_generator in methods[group_size]:
            params = parameter_func(groups_per_round)

            if params is not None:
                t, q = params
                return cls(groups_per_round, group_size, t, q, round_generator, participant_labels)

        return None
