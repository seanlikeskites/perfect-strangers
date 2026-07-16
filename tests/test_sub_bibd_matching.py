# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.sub_bibd_matcher import SubBIBDMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("groups_per_round", [11, 19, 27])
def test_sub_bibd(groups_per_round):
    matcher = SubBIBDMatcher.create_matcher(groups_per_round, 3, [])

    if matcher is not None:
        # Sub-BIBD matching should always give the maximum possible rounds.
        assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, 3)

        # Validate generated rounds
        validate_matcher(matcher)
