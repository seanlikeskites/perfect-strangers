# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

from collections.abc import Sequence
from random import shuffle

import numpy as np

from perfect_strangers.design_types import DesignType, PartialType, RBIBDType, RGDDType
from perfect_strangers.util import is_round_pair_valid, is_round_valid

GroupingMatrix = Sequence[Sequence]
RoundSequence = Sequence[GroupingMatrix]
NumpyRounds = Sequence[np.typing.NDArray]
ParticipantLabels = Sequence | None

class IncorrectParticipantLabelsError(Exception):
    def __init__(self, n_participants, n_labels):
        super().__init__(f"Experiment has {n_participants} participants, but {n_labels} labels provided.")

class NonUniqueParticipantLabelsError(Exception):
    def __init__(self, n_participants, n_labels):
        super().__init__(f"Experiment has {n_participants} participants, but only {n_labels} unique labels provided.")

class BaseMatcher:
    """
    Base class for all group matching methods.
    """
    def __init__(self,
                 groups_per_round: int | None=None,
                 group_size: int | None=None,
                 round_sequence: RoundSequence | None=None,
                 participant_labels: ParticipantLabels=None):
        if round_sequence is not None:
            self._from_round_sequence(round_sequence)
        elif groups_per_round is not None and group_size is not None:
            self._from_experiment_parameters(groups_per_round, group_size)
        else:
            error = "Construction of BaseMatcher requires either experiment parameters or a round_sequnce."
            raise TypeError(error)

        self._participant_labels = participant_labels
        self._validate_participant_labels()

        self.shuffle_sequence()

    def _from_round_sequence(self, round_sequence: RoundSequence):
        self.groups_per_round = len(round_sequence[0])
        self.group_size = len(round_sequence[0][0])

        self.n_participants = self.groups_per_round * self.group_size

        participants = {
            participant: ID
            for ID, participant in enumerate(sorted({p for r in round_sequence for g in r for p in g}))
        }

        self._group_matrices = [
            np.array([
                [participants[p] for p in r]
                for r in g
            ]) for g in round_sequence
        ]

        if not self.validate_rounds():
            error = "Provided round sequence incorrect."
            raise ValueError(error)

    def _from_experiment_parameters(self, groups_per_round: int, group_size: int):
        self.groups_per_round = groups_per_round
        self.group_size = group_size
        self.n_participants = self.groups_per_round * self.group_size

        self._group_matrices = [
            np.arange(self.n_participants).reshape(self.groups_per_round, self.group_size)
        ]

        if groups_per_round >= group_size:
            self._generate_rounds()

    @property
    def max_rounds(self) -> int:
        """
        The maximum number of rounds this matcher will produce under perfect stranger matching conditions.
        """
        return len(self._group_matrices)

    def groups_for_round(self, round_index: int) -> GroupingMatrix:
        """
        Get the groups for the round with a given index.

        :param round_index: The index of the round to get groups for, an integer between `0` and `self.max_rounds - 1`.

        :return: A list of participants groupings for the requested round.
        """
        g = self._group_matrices[round_index].tolist()

        if self._participant_labels is not None:
            g = [
                [self._participant_labels[p] for p in r]
                for r in g
            ]

        return g

    def groups_for_next_round(self) -> GroupingMatrix | None:
        """
        Get the groups for the next round.

        :return: A list of participants groupings for the next round, or None if there are no more rounds possible.
        """
        if self.next_round >= self.max_rounds:
            return None

        g = self.groups_for_round(self.next_round)
        self.next_round += 1
        return g

    def restart(self):
        """
        Reset the matcher to the first round.
        """
        self.next_round = 0

    @property
    def rounds(self) -> RoundSequence:
        """
        A list of participant groupings for all rounds constructed by this matcher.
        """
        return [self.groups_for_round(i) for i in range(self.max_rounds)]

    def __iter__(self):
        """
        Allow for iterating over rounds in a for loop. For example:

            matcher = create_matcher(groups_per_round, group_size)

            for round in matcher:
                print(round)
        """
        return iter(self.rounds)

    def shuffle_sequence(self):
        """
        Shuffle the list of rounds produced by this matcher.
        """
        shuffle(self._group_matrices)
        self.restart()

    def _generate_rounds(self):
        pass

    def _append_round(self, g):
        if not is_round_valid(g, self.groups_per_round, self.group_size):
            return False

        for r in self._group_matrices:
            if not is_round_pair_valid(r, g):
                return False

        self._group_matrices.append(g)
        return True

    def sub_matcher(self, groups_per_round: int) -> BaseMatcher | None:
        if groups_per_round == 1:
            group = self.groups_for_round(0)[0]
            return BaseMatcher(round_sequence=[[group]], participant_labels=group)

        return None

    def _design_type(self) -> DesignType | None:
        return None

    def design_type(self) -> DesignType:
        subclass_type = self._design_type()

        if subclass_type is not None:
            return subclass_type

        numerator = self.n_participants - 1
        denominator = self.group_size - 1
        quotient = numerator // denominator
        remainder = numerator % denominator

        if self.max_rounds == quotient:
            if remainder == 0:
                return RBIBDType(self.n_participants, self.group_size)

            group_size = remainder + 1
            return RGDDType(self.group_size, remainder + 1, self.n_participants // group_size)

        return PartialType()

    def validate_rounds(self) -> bool:
        for i, current_round in enumerate(self._group_matrices):
            # Check current round include all participants.
            if not is_round_valid(current_round, self.groups_per_round, self.group_size):
                return False

            # Check all subsequent rounds preserve perfect stranger matching with
            # current round.
            for j in range(i + 1, self.max_rounds):
                next_round = self._group_matrices[j]

                if not is_round_pair_valid(current_round, next_round):
                    return False

        return True

    def _validate_participant_labels(self):
        if self._participant_labels is not None:
            if len(self._participant_labels) != self.n_participants:
                raise IncorrectParticipantLabelsError(self.n_participants, len(self._participant_labels))

            if len(set(self._participant_labels)) != self.n_participants:
                raise NonUniqueParticipantLabelsError(self.n_participants, len(set(self._participant_labels)))

