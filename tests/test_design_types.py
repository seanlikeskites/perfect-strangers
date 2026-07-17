# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from perfect_strangers import create_matcher
from perfect_strangers.design_types import RBIBDType, RGDDType, RTDType
from perfect_strangers.util import sequence_length_upper_bound


@pytest.mark.parametrize("group_size", range(2, 7))
@pytest.mark.parametrize("groups_per_round", range(2, 28))
def test_design_types(groups_per_round, group_size):
    matcher = create_matcher(groups_per_round, group_size)
    design_type = matcher.design_type()
    upper_bound = sequence_length_upper_bound(groups_per_round, group_size)

    if isinstance(design_type, (RBIBDType, RGDDType)):
        assert matcher.max_rounds == upper_bound
    elif isinstance(design_type, RTDType):
        assert matcher.max_rounds == groups_per_round

