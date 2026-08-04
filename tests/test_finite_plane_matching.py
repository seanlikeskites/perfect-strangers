# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.finite_plane_matcher import FinitePlaneMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(3, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_finite_plane(groups_per_round, group_size):
    matcher = FinitePlaneMatcher.create_matcher(groups_per_round, group_size)

    if matcher is not None:
        if groups_per_round == group_size:
            assert matcher.max_rounds == groups_per_round + 1
        elif matcher._plane_order == groups_per_round:
            assert matcher.max_rounds >= groups_per_round

        # Validate generated rounds
        validate_matcher(matcher)
