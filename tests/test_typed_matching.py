# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import pytest

from perfect_strangers import create_typed_matcher
from perfect_strangers.matchers import (
    ColumnShiftMatcher,
    FinitePlaneMatcher,
)
from perfect_strangers.util import (
    group_size_from_spec,
    least_prime_factor,
    sequence_length_upper_bound,
    unique_integers_summing_to_n,
)
from tests.matcher_validation import validate_matcher

group_specs = [
    spec
    for group_size in range(2, 7)
    for spec in unique_integers_summing_to_n(group_size)
]

@pytest.mark.parametrize("group_spec", group_specs)
@pytest.mark.parametrize("groups_per_round", range(2, 28))
def test_typed_matching(groups_per_round, group_spec):
    matcher = create_typed_matcher(groups_per_round, group_spec)

    # Validate generated rounds
    validate_matcher(matcher)

    # Check create_typed_matcher selected the best performing algorithm.
    algorithms = [
        ColumnShiftMatcher(groups_per_round, group_spec),
        FinitePlaneMatcher.create_matcher(groups_per_round, group_spec),
    ]

    assert matcher.max_rounds == max(a.max_rounds for a in algorithms if a is not None)

    # Check typed matching respects returned typings.
    for r in matcher.rounds:
        for g in r:
            for i, n in enumerate(group_spec):
                assert len(set(g) & set(matcher.participant_types[i])) == n

    # Test optimal situations
    group_size = group_size_from_spec(group_spec)

    if len(group_spec) > 1 and (group_size <= least_prime_factor(groups_per_round) or
                                galois.is_prime_power(groups_per_round)):
        assert matcher.max_rounds == sequence_length_upper_bound(groups_per_round, group_spec)
