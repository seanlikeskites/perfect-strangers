# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import RoundRobinMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_round_robin(groups_per_round):
    matcher = RoundRobinMatcher(groups_per_round)

    # Round robin matching should always give the maximum possible rounds.
    assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, 2)

    # Validate generated rounds
    validate_matcher(matcher)
