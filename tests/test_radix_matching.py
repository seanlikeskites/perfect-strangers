# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.radix_matcher import RadixMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("exponent", range(2, 4))
def test_radix_matching(group_size, exponent):
    matcher = RadixMatcher(group_size, exponent)

    # Validate generated rounds
    validate_matcher(matcher)
