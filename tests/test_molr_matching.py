# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import MOLRMatcher
from tests.matcher_validation import validate_matcher

test_cases = [
    (6, 3),
    (6, 4),
    (6, 5)
]

@pytest.mark.parametrize(("groups_per_round", "group_size"), test_cases)
def test_molr(groups_per_round, group_size):
    matcher = MOLRMatcher.create_matcher(groups_per_round, [group_size])

    # Validate generated rounds
    validate_matcher(matcher)
