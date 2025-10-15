# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Sequence

import numpy as np

from perfect_strangers.util import is_round_pair_valid, is_round_valid

RoundSequence = Sequence[np.typing.NDArray]

class BaseMatcher:
    def __init__(self, groups_per_round: int, group_size: int):
        self.groups_per_round = groups_per_round
        self.group_size = group_size
        self.n_participants = groups_per_round * group_size

        self.group_matrices = [
            np.arange(self.n_participants).reshape(self.groups_per_round, self.group_size)
        ]

        self._generate_rounds()

        self.next_round = 0

    @property
    def max_rounds(self) -> int:
        return len(self.group_matrices)

    def groups_for_next_round(self) -> list[list[int]] | None:
        if self.next_round >= self.max_rounds:
            return None

        g = self.group_matrices[self.next_round].tolist()
        self.next_round += 1
        return g

    def _generate_rounds(self):
        pass

    def _append_round(self, g):
        if not is_round_valid(g, self.groups_per_round, self.group_size):
            return False

        for r in self.group_matrices:
            if not is_round_pair_valid(r, g):
                return False

        self.group_matrices.append(g)
        return True

    def validate_rounds(self) -> bool:
        for i, current_round in enumerate(self.group_matrices):
            # Check current round include all participants.
            if not is_round_valid(current_round, self.groups_per_round, self.group_size):
                return False

            # Check all subsequent rounds preserve perfect stranger matching with
            # current round.
            for j in range(i + 1, self.max_rounds):
                next_round = self.group_matrices[j]

                if not is_round_pair_valid(current_round, next_round):
                    return False

        return True
