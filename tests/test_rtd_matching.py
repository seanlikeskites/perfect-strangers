# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import RTDMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_rtd(groups_per_round, group_size):
    matcher = RTDMatcher.create_matcher(groups_per_round, group_size)

    if matcher is not None:
        # Kirkman triple matching should always give a number of rounds equal to the number of groups per round.
        assert matcher.max_rounds == groups_per_round

        # Validate generated rounds
        validate_matcher(matcher)
