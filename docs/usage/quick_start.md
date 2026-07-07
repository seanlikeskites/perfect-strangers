# Quick Start
## Installation

```Shell
pip install perfect-strangers
```

## Create a Matcher
To get started import the [`create_matcher()`](matcher_objects.md#perfect_strangers.create_matcher) function:

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

For each round of the experiment call
[`groups_for_next_round()`](matcher_objects.md#perfect_strangers.BaseMatcher.groups_for_next_round) on the matcher object to
get the participant groupings.

```Python
groups = matcher.groups_for_next_round()
```

Alternatively, one can loop over the rounds like so:

```Python
for groups in matcher:
    print(groups)
```

Participant grouping for a round are returned as a list of lists, each list containing the participant labels for the
members of a single group.

```Python
>>> print(matcher.groups_for_next_round())
[[8, 9, 14], [10, 0, 13], [12, 6, 3], [2, 4, 11], [7, 5, 1]]
```

## Participant Labels
By default, the experiment participants are identified by the integers between `0` and `N - 1` where `N` is the total number
of participants. If your participants are otherwise identified, you can provide a list of participant labels to the
`participant_labels` parameter of [`create_matcher()`](matcher_objects.md#perfect_strangers.create_matcher). This must be a
list of `N` unique values.

For example, to label the participants from `1` to `N` (as oTree does) we can define the participant labels like so.

```Python
groups_per_round = 5 # Number of groups per round of the experiment.
group_size = 3 # Number of participants per group.
n_participants = groups_per_round * group_size

matcher = create_matcher(groups_per_round,
                         group_size, 
                         participant_labels=range(1, n_participants + 1))
```
