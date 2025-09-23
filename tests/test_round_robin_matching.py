# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from tests.matcher_verifications import verify_matcher


@pytest.mark.parametrize("groups_per_round", range(2, 21))
def test_round_robin(groups_per_round):
    matcher = create_matcher(groups_per_round, 2)

    # Round robin matching should always give the maximum possible rounds.
    assert matcher.max_rounds == 2 * groups_per_round - 1

    # Verify generated rounds
    verify_matcher(matcher)
