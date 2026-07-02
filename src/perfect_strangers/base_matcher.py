# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

from collections.abc import Sequence
from random import shuffle

import numpy as np

from perfect_strangers.util import is_round_pair_valid, is_round_valid

RoundSequence = Sequence[np.typing.NDArray]
RoundGroups = list[list]
ParticipantLabels = list | None

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
    def __init__(self, groups_per_round: int, group_size: int, participant_labels: ParticipantLabels):
        self.groups_per_round = groups_per_round
        self.group_size = group_size
        self.n_participants = groups_per_round * group_size
        self._participant_labels = participant_labels

        self._validate_participant_labels()

        self._group_matrices = [
            np.arange(self.n_participants).reshape(self.groups_per_round, self.group_size)
        ]

        if groups_per_round >= group_size:
            self._generate_rounds()

        self.shuffle_sequence()

    @property
    def max_rounds(self) -> int:
        """
        The maximum number of rounds this matcher will produce under perfect stranger matching conditions.
        """
        return len(self._group_matrices)

    def groups_for_round(self, round_index: int) -> RoundGroups:
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

    def groups_for_next_round(self) -> RoundGroups | None:
        """
        Get the groups for the next round.

        :return: A list of participants groupings for the next round, or None if there a no more rounds possible.
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
    def rounds(self) -> list[list[list]]:
        """
        A list of participant groupings for all possible rounds constructed by this matcher.
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
