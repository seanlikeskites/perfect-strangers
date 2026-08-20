# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import PrimitiveElementMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", [3, 4])
@pytest.mark.parametrize("groups_per_round", range(3, 31))
def test_primitive_element(groups_per_round, group_size):
    matcher = PrimitiveElementMatcher.create_matcher(groups_per_round, group_size)

    if matcher is not None:
        # Primitive element matching should always give the maximum possible rounds.
        assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)

        # Validate generated rounds
        validate_matcher(matcher)
