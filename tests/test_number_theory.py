# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest
from sympy.ntheory import isprime, primefactors, primerange  # type: ignore

from perfect_strangers.util import is_prime, least_prime_factor, unique_prime_factors, root_of_prime_power


@pytest.mark.parametrize("n", range(101))
def test_prime_test(n):
    assert not (is_prime(n) ^ isprime(n))

@pytest.mark.parametrize("n", range(101))
def test_prime_factors(n):
    test_value = unique_prime_factors(n)
    truth = primefactors(n)

    assert test_value == set(truth)

@pytest.mark.parametrize("n", range(101))
def test_least_prime_factor(n):
    test_value = least_prime_factor(n)

    if n < 2:
        assert test_value is None

    else:
        truth = min(primefactors(n))
        assert test_value == truth

@pytest.mark.parametrize("n", range(1, 10))
@pytest.mark.parametrize("p", primerange(100))
def test_prime_powers(p, n):
    assert root_of_prime_power(p ** n) == p

@pytest.mark.parametrize("c", primerange(10))
@pytest.mark.parametrize("b", primerange(10))
@pytest.mark.parametrize("a", primerange(10))
def test_prime_powers_composites(a, b, c):
    test_value = root_of_prime_power(a * b * c)

    if a == b and b == c:
        assert test_value == a
    else:
        assert test_value is None
