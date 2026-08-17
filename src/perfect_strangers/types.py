# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy.typing as npt

GroupingMatrix = list[list]
RoundSequence = list[GroupingMatrix]
NumpyRounds = list[npt.NDArray]
GroupSpec = Sequence[int]
