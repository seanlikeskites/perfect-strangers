# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from perfect_strangers.util import round_to_sets, sequence_length_upper_bound


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

def validate_sub_matchers(matcher, should_be_bibds=False):
    for s in matcher.available_sub_matchers():
        sub_matcher = matcher.sub_matcher(s)

        assert sub_matcher.groups_per_round == s

        validate_matcher(sub_matcher)

        round_sets = [round_to_sets(r) for r in matcher.rounds]
        sub_sets = [round_to_sets(r) for r in sub_matcher.rounds]

        for sub_round in sub_sets:
            assert any(sub_round < rnd for rnd in round_sets)

        if should_be_bibds:
            assert sub_matcher.max_rounds == sequence_length_upper_bound(s, matcher.group_size)
