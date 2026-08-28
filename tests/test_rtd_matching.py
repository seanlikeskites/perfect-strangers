# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import RTDMatcher
from tests.matcher_validation import validate_matcher

test_cases = [
    (10, 3),
    (12, 3),
    (12, 4),
    (12, 5),
    (12, 6)
]

@pytest.mark.parametrize(("groups_per_round", "group_size"), test_cases)
def test_rtd(groups_per_round, group_size):
    matcher = RTDMatcher.create_matcher(groups_per_round, [group_size])

    # LBR matching should always give the maximum possible rounds.
    assert matcher.max_rounds == groups_per_round

    # Validate generated rounds
    validate_matcher(matcher)
