# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers.sub_bibd_matcher import SubBIBDMatcher
from perfect_strangers.util import sequence_length_upper_bound
from tests.matcher_validation import validate_matcher

test_cases = [
    # Groups of 3
    (11, 3),
    (15, 3),
    (19, 3),
    (21, 3),
    (27, 3),

    # Groups of 4
    (16, 4),
    (19, 4)
]

@pytest.mark.parametrize(("groups_per_round", "group_size"), test_cases)
def test_sub_bibd(groups_per_round, group_size):
    matcher = SubBIBDMatcher.create_matcher(groups_per_round, group_size, [])

    # Sub-BIBD matching should always give the maximum possible rounds.
    assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)
