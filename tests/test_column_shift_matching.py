# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from tests.matcher_verifications import verify_matcher


@pytest.mark.parametrize("groups_per_round", range(2, 21))
@pytest.mark.parametrize("group_size", range(3, 7))
def test_column_shifts(groups_per_round, group_size):
    matcher = create_matcher(groups_per_round, group_size)

    # Verify generated rounds
    verify_matcher(matcher)
