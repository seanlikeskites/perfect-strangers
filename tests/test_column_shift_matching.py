# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import ColumnShiftMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_column_shifts(groups_per_round, group_size):
    matcher = ColumnShiftMatcher(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)
