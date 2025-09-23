# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import numpy as np


class BaseMatcher:
    def __init__(self, groups_per_round, group_size):
        self.groups_per_round = groups_per_round
        self.group_size = group_size
        self.n_participants = groups_per_round * group_size

        self.group_matrices = [
            np.arange(self.n_participants).reshape(self.groups_per_round, self.group_size)
        ]

        self._generate_rounds()

        self.next_round = 0

    @property
    def max_rounds(self):
        return len(self.group_matrices)

    def groups_for_next_round(self):
        if self.next_round >= self.max_rounds:
            return None

        g = self.group_matrices[self.next_round].tolist()
        self.next_round += 1
        return g

    def _generate_rounds(self):
        pass

