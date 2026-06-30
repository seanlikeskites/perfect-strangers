# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

import galois
import numpy as np

from perfect_strangers.base_matcher import BaseMatcher


class RTDMatcher(BaseMatcher):
    def __init__(self, groups_per_round: int, group_size: int):
        super().__init__(groups_per_round, group_size)

    def _generate_rounds(self):
        labels = np.arange(self.n_participants).reshape(self.groups_per_round, self.group_size)

        gf = galois.GF(self.groups_per_round)
        rounds = []

        for r in range(self.groups_per_round):
            new_round = np.empty((self.groups_per_round, self.group_size), dtype="int")

            for g in range(self.groups_per_round):
                new_round[g, :] = [labels[gf(g) + gf(r) * gf(p), p] for p in range(self.group_size)]

            rounds.append(new_round)

        self.group_matrices = rounds

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int):
        if galois.is_prime_power(groups_per_round) and group_size <= groups_per_round:
            return RTDMatcher(groups_per_round, group_size)

        return None
