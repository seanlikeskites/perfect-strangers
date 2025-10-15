# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest
import galois

from perfect_strangers.util import least_prime_factor


@pytest.mark.parametrize("n", range(101))
def test_least_prime_factor(n):
    test_value = least_prime_factor(n)

    if n < 2:
        assert test_value is None

    else:
        truth = min(galois.factors(n)[0])
        assert test_value == truth
