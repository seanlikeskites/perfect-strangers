# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

class IncorrectParticipantLabelsError(Exception):
    def __init__(self, type_counts, label_counts):
        if isinstance(type_counts, list):
            super().__init__(f"Experiment has {type_counts} participants of each type but participant_labels with " \
                             f"shape {label_counts} provided.")
        else:
            super().__init__(f"Experiment has {type_counts} participants but {label_counts} labels provided.")

class NonUniqueParticipantLabelsError(Exception):
    def __init__(self, n_participants, n_labels):
        super().__init__(f"Experiment has {n_participants} participants but only {n_labels} unique labels provided.")


