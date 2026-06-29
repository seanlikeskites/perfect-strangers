# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 14))
def test_benchmarks(groups_per_round, group_size):
    matcher = create_matcher(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)
