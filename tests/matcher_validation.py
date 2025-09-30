# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

def verify_n_rounds(matcher):
    n_rounds = 0

    while matcher.groups_for_next_round() is not None:
        n_rounds += 1

    assert n_rounds == matcher.max_rounds


def validate_matcher(matcher):
    if matcher.groups_per_round >= matcher.group_size:
        assert matcher.max_rounds > 1
    else:
        assert matcher.max_rounds == 1

    verify_n_rounds(matcher)

    assert matcher.validate_rounds()
