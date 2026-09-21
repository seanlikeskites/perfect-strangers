# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import ColumnShiftMatcher
from perfect_strangers.util import least_prime_factor
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_column_shifts(groups_per_round, group_size):
    matcher = ColumnShiftMatcher(groups_per_round, [group_size])

    # Validate generated rounds
    validate_matcher(matcher)

    # Test optimal situations
    if group_size <= least_prime_factor(groups_per_round):
        assert matcher.max_rounds == groups_per_round
