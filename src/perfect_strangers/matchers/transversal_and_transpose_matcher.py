# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy as np

from perfect_strangers.matchers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.matchers.finite_plane_matcher import FinitePlaneMatcher
from perfect_strangers.matchers.mols_matcher import MOLSMatcher
from perfect_strangers.matchers.typed_matcher import TypedMatcher
from perfect_strangers.types import GroupSpec, NumpyRounds
from perfect_strangers.util import submatrix_transpositions, use_finite_plane_construction


def _get_transversal_matcher_rounds(groups_per_round: int, group_size: int) -> NumpyRounds:
    group_spec = [group_size]

    m = MOLSMatcher.create_matcher(groups_per_round, group_spec)

    if m is None:
        if use_finite_plane_construction(groups_per_round, group_spec):
            m = FinitePlaneMatcher.create_matcher(groups_per_round, group_spec)
        else:
            m = ColumnShiftMatcher(groups_per_round, group_spec)

    return m._group_matrices

def _round_from_sub_matrices(round_template: np.typing.NDArray, sub_matrices: NumpyRounds) -> np.typing.NDArray:
    r = []

    for s in sub_matrices:
        matching_ids = s.flatten()

        r.extend([
            [matching_ids[p] for p in g]
            for g in round_template
        ])

    return np.array(r)


def _get_transposition_rounds(transposed_matrix: np.typing.NDArray, block_size: int) -> NumpyRounds:
    n_blocks = transposed_matrix.shape[0] // block_size
    group_size = transposed_matrix.shape[1]

    sub_matrices = [
        transposed_matrix[b::block_size, :] for b in range(block_size)
    ]

    transposed_rounds = _get_transversal_matcher_rounds(n_blocks, group_size)

    return [
        _round_from_sub_matrices(r, sub_matrices)
        for r in transposed_rounds
    ]

class TransversalAndTransposeMatcher(TypedMatcher):
    """
    Matcher to select the best transversal design method and apply submatrix transposition if possible.
    """
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 participant_labels: Sequence | None=None):

        super().__init__(groups_per_round, group_spec, participant_labels=participant_labels)

    def _generate_typed_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        rounds = _get_transversal_matcher_rounds(self.groups_per_round, self.group_size)

        if self._more_than_one_participant_type():
            return rounds

        participants = initial_groupings.copy()

        # Apply submatrix transposition.
        transpositions = submatrix_transpositions(participants)

        self._performed_transposition = len(transpositions) > 0

        for t, s in transpositions:
            rounds += _get_transposition_rounds(t, s)

        return rounds
