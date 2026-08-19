# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy as np

from perfect_strangers.exceptions import IncorrectParticipantLabelsError, NonUniqueParticipantLabelsError
from perfect_strangers.matchers.base_matcher import BaseMatcher
from perfect_strangers.types import GroupSpec, NumpyRounds
from perfect_strangers.util import is_round_valid


class TypedMatcher(BaseMatcher):
    """
    Base class for matchers which perform typed perfect stranger matching.
    """

    ##################################################################
    # Initialisation
    ##################################################################
    def __init__(self,
                 groups_per_round: int,
                 group_spec: GroupSpec,
                 participant_labels: Sequence | None=None):

        self.group_spec = list(group_spec)
        group_size = sum(group_spec)

        self._auto_type = False

        super().__init__(groups_per_round, group_size, participant_labels=participant_labels)

    def _generate_typed_rounds(self, _initial_groupings: np.typing.NDArray) -> NumpyRounds:
        return []

    def _generate_rounds(self, initial_groupings: np.typing.NDArray) -> NumpyRounds:
        return self._generate_typed_rounds(initial_groupings)

    def _init_participant_label_map(self, initial_groupings: np.typing.NDArray):
        def get_columns(i):
            start_index = sum(self.group_spec[0:i])
            end_index = start_index + self.group_spec[i]

            return initial_groupings[:, start_index:end_index].flatten().tolist()

        self._participant_types = [
            get_columns(i) for i in range(len(self.group_spec))
        ]

        self._participant_label_map = None

        if self._auto_type:
            super()._init_participant_label_map(initial_groupings)
        elif self._participant_labels is not None:
            self._participant_label_map = {
                p: self._participant_labels[i][j]
                for i, t in enumerate(self._participant_types)
                for j, p in enumerate(t)
            }

    ##################################################################
    # Info
    ##################################################################
    def _more_than_one_participant_type(self) -> bool:
        return len(self.group_spec) > 1

    @property
    def participant_types(self) -> list[list]:
        """
        A list of lists detailing which participants are of witch type. The n^th^ list contains the participants identifiers
        for the n^th^ participant type.
        """
        if self._participant_label_map is None:
            return self._participant_types

        return [
            [self._participant_label_map[i] for i in t]
            for t in self._participant_types
        ]

    ##################################################################
    # Validation
    ##################################################################
    def _validate_participant_labels(self):
        if self._participant_labels is not None:
            if len(self._participant_labels) != len(self.group_spec):
                self._auto_type = True
                super()._validate_participant_labels()

            else:
                type_counts = [t * self.groups_per_round for t in self.group_spec]

                try:
                    label_counts = [len(t) for t in self._participant_labels]
                except TypeError:
                    error = "Participant labels should be a sequence of sequences."
                    raise ValueError(error) from None

                if label_counts != type_counts:
                    raise IncorrectParticipantLabelsError(type_counts, label_counts)

                n_unique_labels = len({
                    l for t in self._participant_labels for l in t
                })

                if n_unique_labels != self.n_participants:
                    raise NonUniqueParticipantLabelsError(self.n_participants, n_unique_labels)

    def _is_round_valid(self, g: np.typing.NDArray) -> bool:
        participant_types_sets = [set(p) for p in self._participant_types]

        for group in g:
            group_set = set(group)

            for i, count in enumerate(self.group_spec):
                if len(group_set & participant_types_sets[i]) != count:
                    return False

        return is_round_valid(g, self.groups_per_round, self.group_size)
