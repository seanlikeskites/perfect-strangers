# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest
from sympy import primefactors

from perfect_strangers.column_shift_matcher import _least_prime_factor


@pytest.mark.parametrize("n", range(101))
def test_least_prime_factor(n):
    test_value = _least_prime_factor(n)

    if n < 2:
        assert test_value is None

    else:
        truth = min(primefactors(n))
        assert test_value == truth
