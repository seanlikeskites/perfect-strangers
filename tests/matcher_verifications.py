# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

def verify_n_rounds(matcher):
    n_rounds = 0

    while matcher.groups_for_next_round() is not None:
        n_rounds += 1

    assert n_rounds == matcher.max_rounds

def verify_perfect_strangers(matcher):
    gs = matcher.group_matrices
    n_rounds = len(gs)

    for i in range(n_rounds - 1):
        r1 = gs[i]

        for j in range(i + 1, n_rounds):
            r2 = gs[j]

            for k in range(r1.shape[0]):
                g1 = set(r1[k, :])

                for l in range(r2.shape[0]):
                    g2 = set(r2[l, :])

                    if len(g1 & g2) > 1:
                        return False

    return True

def verify_matcher(matcher):
    if matcher.groups_per_round >= matcher.group_size:
        assert matcher.max_rounds > 1
    else:
        assert matcher.max_rounds == 1

    verify_n_rounds(matcher)

    assert verify_perfect_strangers(matcher)
