# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from tests.matcher_validation import validate_sub_matchers


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 28))
def test_sub_matchers(groups_per_round, group_size):
    matcher = create_matcher(groups_per_round, group_size)

    # All matchers should have a 1 round sub_matcher
    assert 1 in matcher.available_sub_matchers()

    validate_sub_matchers(matcher)

