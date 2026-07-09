# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json

import numpy as np

from perfect_strangers.base_matcher import BaseMatcher, ParticipantLabels


#######################################################################
# Matcher
#######################################################################
class NearlyKirkmanTripleMatcher(BaseMatcher):
    """ Constructions of NKTSs as per doi.org/10.1002/jcd.21342 """
    def __init__(self, starters: list[list], participant_labels: ParticipantLabels=None):
        self.starters = starters

        super().__init__(len(starters), 3, participant_labels)

    def _shift_group_member(self, participant: int, round_index: int) -> int:
        mod = self.n_participants - 2

        if participant < mod:
            return (participant + 2 * round_index) % mod
        # The final two participants are the two infinity points from the paper
        # so do not shift.
        return participant

    def _round_groups(self, round_index: int) -> np.typing.NDArray:
        shifts = [
            [self._shift_group_member(p, round_index) for p in s]
            for s in self.starters
        ]

        return np.array(shifts)

    def _generate_rounds(self):
        n_rounds = self.n_participants // 2 - 1

        self._group_matrices = []

        for round_index in range(n_rounds):
            self._group_matrices.append(self._round_groups(round_index))

    @classmethod
    def create_matcher(cls, groups_per_round: int, participant_labels: ParticipantLabels=None):
        with importlib.resources.files("perfect_strangers").joinpath("lookup/nkts_starters.json").open() as f:
            starting_groups = json.loads(f.read())

        try:
            return NearlyKirkmanTripleMatcher(starting_groups[str(groups_per_round * 3)], participant_labels)
        except KeyError:
            return None
