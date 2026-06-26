# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

import galois

from perfect_strangers import ColumnShiftMatcher
from perfect_strangers.util import sequence_length_upper_bound, x_is_power_of_y
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_column_shifts(groups_per_round, group_size):
    matcher = ColumnShiftMatcher(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)

    # Test optimal situations
    if galois.is_prime(group_size) and x_is_power_of_y(groups_per_round, group_size):
        assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)
