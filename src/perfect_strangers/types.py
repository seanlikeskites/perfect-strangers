# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>

# SPDX-License-Identifier: MIT

from collections.abc import Sequence

import numpy.typing as npt

GroupingMatrix = Sequence[Sequence]
RoundSequence = Sequence[GroupingMatrix]
NumpyRounds = Sequence[npt.NDArray]
GroupSpec = int | Sequence[int]
