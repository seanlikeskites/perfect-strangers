# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import KirkmanTripleMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("groups_per_round", range(2, 31))
def test_round_robin(groups_per_round):
    matcher = KirkmanTripleMatcher.create_matcher(groups_per_round)

    if matcher is not None:
        # Kirkman triple matching should always give the maximum possible rounds.
        assert matcher.max_rounds == (3 * groups_per_round - 1) // 2

        # Validate generated rounds
        validate_matcher(matcher)
