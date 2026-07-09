# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import NearlyKirkmanTripleMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("groups_per_round", range(8, 13, 2))
def test_nearly_kirkman(groups_per_round):
    matcher = NearlyKirkmanTripleMatcher.create_matcher(groups_per_round)

    # Nearly Kirkman triple matching should always give the maximum possible rounds.
    assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, 3)

    # Validate generated rounds
    validate_matcher(matcher)
