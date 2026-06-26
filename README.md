# perfect_strangers

[![PyPI - Version](https://img.shields.io/pypi/v/perfect-strangers.svg)](https://pypi.org/project/perfect-strangers)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/perfect-strangers.svg)](https://pypi.org/project/perfect-strangers)
![Test Status](https://img.shields.io/github/actions/workflow/status/seanlikeskites/perfect-strangers/tests.yml?label=tests)

-----

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [License](#license)

## Installation

```console
pip install perfect-strangers
```

## Quick Start
### Create a Matcher
To get started import the `create_matcher()` function:

```Python
from perfect_strangers import create_matcher
```

This function returns a group matcher object which will produce the longest sequence of perfect stranger matched rounds for
the given experiment parameters.

```Python
groups_per_round = 5 # Number of groups per round of the experiment.
group_size = 3 # Number of participants per group.

matcher = create_matcher(groups_per_round, group_size)
```

For each round of the experiment call `groups_for_next_round()` on the matcher object to get the participant groupings.

```Python
groups = matcher.groups_for_next_round()
```

## License

`perfect-strangers` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
