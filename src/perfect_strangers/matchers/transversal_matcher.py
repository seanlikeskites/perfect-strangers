# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

from perfect_strangers.design_types import DesignType, RTDType
from perfect_strangers.matchers.typed_matcher import TypedMatcher
from perfect_strangers.types import GroupSpec


class TransversalMatcher(TypedMatcher):
    """
    Base class for matchers which produce Resolvable Transversal Designs (both complete and incomplete).
    """
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 participant_labels: Sequence | None=None):

        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _design_type(self) -> DesignType | None:
        if self.max_rounds == self.groups_per_round:
            return RTDType(self.group_size, self.groups_per_round)

        return None

