# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

class IncorrectParticipantLabelsError(Exception):
    def __init__(self, n_participants, n_labels):
        super().__init__(f"Experiment has {n_participants} participants, but {n_labels} labels provided.")

class NonUniqueParticipantLabelsError(Exception):
    def __init__(self, n_participants, n_labels):
        super().__init__(f"Experiment has {n_participants} participants, but only {n_labels} unique labels provided.")


