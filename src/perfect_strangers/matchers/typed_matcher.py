# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

from perfect_strangers.matchers.base_matcher import BaseMatcher
from perfect_strangers.types import GroupSpec


class TypedMatcher(BaseMatcher):
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec | int,
                 participant_labels: Sequence | None=None):

        if isinstance(group_spec, Sequence):
            self.group_spec = group_spec
            group_size = sum(group_spec)
        else:
            self.group_spec = [int(group_spec)]
            group_size = int(group_spec)

        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)
