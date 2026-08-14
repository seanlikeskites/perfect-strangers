# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.matchers import KirkmanTripleMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("groups_per_round", range(3, 31, 2))
def test_kirkman(groups_per_round):
    matcher = KirkmanTripleMatcher.create_matcher(groups_per_round)

    if matcher is not None:
        # Kirkman triple matching should always give the maximum possible rounds.
        assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, 3)

        # Validate generated rounds
        validate_matcher(matcher)
