# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import importlib
import json
from typing import TYPE_CHECKING

import numpy as np

from perfect_strangers.matchers.base_matcher import BaseMatcher

if TYPE_CHECKING:
    from collections.abc import Sequence

    from perfect_strangers.types import GroupingMatrix, NumpyRounds, RoundSequence


def _round_from_blocks(blocks: list, gdd_points: np.typing.NDArray) -> GroupingMatrix:
    gdd_group_size = gdd_points.shape[1]

    def col_for_point(i: int, j: int, labels: list):
        if i == 0:
            return j

        return (j + labels[i - 1]) % gdd_group_size

    return [
        [gdd_points[p, col_for_point(i, j, b["labels"])] for i, p in enumerate(b["points"])]
        for b in blocks
        for j in range(gdd_group_size)
    ]

def _rounds_from_lrb_classes(lrb: dict, gdd_points: np.typing.NDArray) -> RoundSequence:
    return [_round_from_blocks(c["blocks"], gdd_points) for c in lrb["classes"]]

def _rounds_from_lrb_base_blocks(lrb: dict, gdd_points: np.typing.NDArray) -> RoundSequence:
    mod_index = lrb["mod"]

    def shift_block(block, shift):
        shifted = block.copy()

        shifted["points"] = [
            (p + shift) % mod_index if p < mod_index else p for p in shifted["points"]
        ]

        return shifted

    rounds = []

    for i in range(mod_index):
        blocks = [shift_block(b, i) for b in lrb["base_blocks"]]
        rounds.append(_round_from_blocks(blocks, gdd_points))

    return rounds

class LRBMatcher(BaseMatcher):
    """
    Class to construct a (k, 1)-RGDD of type (k-1)^v from a LRB(k, k - 1, v) as per Shen (1992).
    """
    def __init__(self, k: int, m: int, v: int, lrb: dict, participant_labels: Sequence | None=None):
        self._lrb_lambda = m
        self._lrb_n_points = v
        self._lrb = lrb

        super().__init__((v * m) // k, k, participant_labels=participant_labels)

    def _generate_rounds(self, _initial_groupings: np.typing.NDArray) -> NumpyRounds:
        gdd_points = np.arange(self.n_participants).reshape(self._lrb_n_points, self._lrb_lambda)

        rounds = []

        if "classes" in self._lrb:
            rounds = _rounds_from_lrb_classes(self._lrb, gdd_points)
        elif "base_blocks" in self._lrb:
            rounds = _rounds_from_lrb_base_blocks(self._lrb, gdd_points)

        return [np.array(r) for r in rounds]

    @classmethod
    def create_matcher(cls, groups_per_round: int, group_size: int, participant_labels: Sequence | None=None):
        with importlib.resources.files("perfect_strangers").joinpath("data/labeled_resolvable_designs.json").open() as f:
            design_data = json.loads(f.read())

        lrb_block_size = group_size

        n_participants = groups_per_round * group_size

        for lrb_lambda in range(1, lrb_block_size):
            if n_participants % lrb_lambda != 0:
                continue

            lrb_n_points = n_participants // lrb_lambda

            try:
                lrb = design_data[str(lrb_block_size)][str(lrb_lambda)][str(lrb_n_points)]
                return cls(lrb_block_size, lrb_lambda, lrb_n_points, lrb, participant_labels=participant_labels)

            except KeyError:
                continue

        return None
