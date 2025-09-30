# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.base_matcher import BaseMatcher


def _round_increments(group_size, exponent):
    for n in range(1, exponent):
        leading_one = group_size ** n

        for i in range(leading_one):
            yield leading_one + i

def _non_carry_add_base_s(a, b, s):
    n = 0
    c = 0

    while a + b > 0:
        c += s**n * (((a % s) + (b % s)) % s)
        n += 1
        a //= s
        b //= s

    return c

def _make_group(group_size, first_member, increment):
    m = first_member
    remaining = group_size

    group = []

    while remaining > 0:
        group.append(m)
        m = _non_carry_add_base_s(m, increment, group_size)
        remaining -= 1

    return group

class RadixMatcher(BaseMatcher):
    def __init__(self, group_size, exponent):
        self.exponent = exponent
        super().__init__(group_size ** (exponent - 1), group_size)

    def _generate_rounds(self):
        participants = set(range(self.n_participants))

        for i in _round_increments(self.group_size, self.exponent):
            allocated = set()
            g = self.group_matrices[0].copy()

            for j in range(self.groups_per_round):
                first_member = min(participants - allocated)
                next_group = _make_group(self.group_size, first_member, i)
                g[j, :] = next_group
                allocated.update(set(next_group))

            self._append_round(g)
