# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy.typing as npt


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

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def unique_prime_factors(n: int) -> set[int]:
    factors: set[int] = set()

    if n < 2:
        return factors

    f = 2

    while f <= math.sqrt(n):
        while n % f == 0:
            factors.add(f)
            n //= f

        if f == 2:
            f += 1
        else:
            f += 2

    if n > 1:
        factors.add(n)

    return factors


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

def root_of_prime_power(n: int) -> int | None:
    factors = unique_prime_factors(n)

    if len(factors) != 1:
        return None

    return factors.pop()

def is_coprime(a: int, b: int) -> bool:
    a_factors = unique_prime_factors(a)
    b_factors = unique_prime_factors(b)

    return len(a_factors & b_factors) == 0

def n_coprime_integers_less_than_n(n: int) -> int:
    return sum(1 for i in range(1, n) if is_coprime(i, n))

def primitive_root_mod_n(n: int) -> int | None:
    # Known cases.
    if n == 2:
        return 1

    if n == 4:
        return 3

    # Other than 2 and 4, the only other numbers with a primitive root are of the
    # form p^k or 2p^k where p is an odd prime.
    if n % 2 != 0:
        pk_root = root_of_prime_power(n)
    else:
        pk_root = root_of_prime_power(n // 2)

    if pk_root is None or pk_root == 2:
        return None

    # Test all numbers and return first valid primitive root.
    for r in range(2, n):
        # Skip candidate which are coprime with n.
        if not is_coprime(r, n):
            continue

        m = 1
        is_root = True

        # A valid primitive root should pass through all integers coprime to n
        # before returning to 1 when raised to successive powers.
        for _ in range(n_coprime_integers_less_than_n(n) - 1):
            m = (m * r) % n

            if m < 2:
                is_root = False
                break

        if is_root:
            return r

    return None
