# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import LRBMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher

test_cases = [
    (6, 4),
    (9, 4),
    (12, 4),
    (18, 4)
]

@pytest.mark.parametrize(("groups_per_round", "group_size"), test_cases)
def test_lrb(groups_per_round, group_size):
    matcher = LRBMatcher.create_matcher(groups_per_round, group_size)

    # LBR matching should always give the maximum possible rounds.
    assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)
