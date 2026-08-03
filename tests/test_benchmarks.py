# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.finite_plane_matcher import FinitePlaneMatcher
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.lookup_matcher import LookupMatcher
from perfect_strangers.nearly_kirkman_triple_matcher import NearlyKirkmanTripleMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher
from perfect_strangers.sub_bibd_matcher import SubBIBDMatcher
from tests.matcher_validation import validate_matcher


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 28))
def test_benchmarks(groups_per_round, group_size):
    matcher = create_matcher(groups_per_round, group_size)

    # Validate generated rounds
    validate_matcher(matcher)

    # Check create_matcher selected the best performing algorithm.
    algorithms = [
        ColumnShiftMatcher(groups_per_round, group_size),
        LookupMatcher.create_matcher(groups_per_round, group_size),
        FinitePlaneMatcher.create_matcher(groups_per_round, group_size),
        SubBIBDMatcher.create_matcher(groups_per_round, group_size, [])
    ]

    match group_size:
        case 2:
            algorithms.append(RoundRobinMatcher(groups_per_round))

        case 3:
            if groups_per_round % 2:
                algorithms.append(KirkmanTripleMatcher.create_matcher(groups_per_round))
            else:
                algorithms.append(NearlyKirkmanTripleMatcher.create_matcher(groups_per_round))

    assert matcher.max_rounds == max(a.max_rounds for a in algorithms if a is not None)
