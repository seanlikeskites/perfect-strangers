# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT


def is_round_valid(g, groups_per_round, group_size):
    n_groups_check = g.shape[0] == groups_per_round
    group_size_check = g.shape[1] == group_size
    participants_check = set(g.flatten()) == set(range(g.size))

    return n_groups_check and group_size_check and participants_check

def is_round_pair_valid(r1, r2):
    for i in range(r1.shape[0]):
        g1 = set(r1[i, :])

        for j in range(r2.shape[0]):
            g2 = set(r2[j, :])

            if len(g1 & g2) > 1:
                return False

    return True
