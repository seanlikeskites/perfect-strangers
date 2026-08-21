# Quick Start
## Installation

```Shell { .copy }
pip install perfect-strangers
```

## Perfect Stranger Matching
To perform [perfect stranger matching](../theory/overview.md#perfect-stranger-matching) import the
[`create_matcher()`](matcher_objects.md#perfect_strangers.create_matcher) function:

```Python { .copy }
from perfect_strangers import create_matcher
```

This function returns a group matcher object which will construct a sequence of perfect stranger matched rounds for the
given experiment parameters.

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

#### Participant Labels
By default the experiment participants are identified by the integers between `0` and `N - 1`, where `N` is the total number
of participants. If your participants are otherwise identified you can provide a list of participant labels to the
`participant_labels` parameter of [`create_matcher()`](matcher_objects.md#perfect_strangers.create_matcher). This must be a
list of `N` unique values.

For example, to label the participants from `1` to `N` (as [oTree](https://www.otree.org/) does) we can define the
participant labels like so.

```Python
groups_per_round = 5 # Number of groups per round of the experiment.
group_size = 3 # Number of participants per group.
n_participants = groups_per_round * group_size

matcher = create_matcher(groups_per_round,
                         group_size, 
                         participant_labels=range(1, n_participants + 1))
```

Participant groupings are then returned from the matcher using these labels.

```Python
>>> print(matcher.groups_for_next_round())
[[9, 10, 15], [11, 1, 14], [13, 7, 4], [3, 5, 12], [8, 6, 2]]
```

## Typed Perfect Stranger Matching
For [typed perfect stranger matching](../theory/overview.md#typed-perfect-stranger-matching) use the
[`create_typed_matcher()`](matcher_objects.md#perfect_strangers.create_typed_matcher) function.

```Python { .copy }
from perfect_strangers import create_typed_matcher
```

The `group_spec` parameter of this function specifies the composition of each group in terms of number of each type of
participant. `group_spec` should be a sequence of integers, one for each type of participant in your experiment. The n^th^
element of this sequence specifies how many participants of the respective type will be in each group.

For example, say we had two types of participant: teachers and students. In each round, each teacher should be matched with
two students, forming groups of 3 participants who have all not met in previous rounds. The `group_spec` for this experiment
would be `[1, 2]`: one participant of the first type (teachers) and 2 of the second (students).

```Python
groups_per_round = 5 # Number of groups per round of the experiment.
group_spec = [1, 2] # Each group consists of 1 participant of the first type
                    # and 2 of the second type.

matcher = create_typed_matcher(groups_per_round, group_spec)
```

By default participants are automatically sorted into types. The `participant_types` property of the matcher details which
participants have been assigned to each type. To specify which participants are of which type provide `participant_labels`
as shown in [Specified Participant Types](#specified-participant-types).

```Python
>>> print(matcher.participant_types)
[[0, 3, 6, 9, 12], [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]]
```

Participant groupings returned from the matcher will be composed of the relevant number of participants from each of these
types.

```Python
print(matcher.groups_for_next_round())
[[0, 7, 14], [3, 10, 2], [6, 13, 5], [9, 1, 8], [12, 4, 11]]
```

### Participant Labels
#### Automatic Participant Types
To continue to have participants sorted into types automatically but provide your own labels, pass a sequence of labels to
the `participant_labels` parameter of [`create_typed_matcher()`](matcher_objects.md#perfect_strangers.create_typed_matcher).
This sequence should have as many elements as participants (i.e. `groups_per_round * sum(group_spec)`).

```Python
import string

groups_per_round = 5
group_spec = [1, 2]
participant_labels = list(string.ascii_lowercase)[0:15]

matcher = create_typed_matcher(groups_per_round,
                               group_spec,
                               participant_labels=participant_labels)

```

The `participant_types` and participant groupings returned from the matcher then use these labels.

```Python
>>> print(matcher.participant_types)
[['a', 'd', 'g', 'j', 'm'], ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'o']]
>>> print(matcher.groups_for_next_round())
[['a', 'k', 'f'], ['d', 'n', 'i'], ['g', 'b', 'l'], ['j', 'e', 'o'], ['m', 'h', 'c']]
```

#### Specified Participant Types
To specify which participants should be assigned to each type, pass a sequence of sequences to the `participant_labels`
parameter. Each sequence should contain the labels for a particular type of participant, the n^th^ sequence having
`groups_per_round * group_spec[n]` elements.

```Python
groups_per_round = 5
group_spec = [1, 2]
participant_labels = [
    [f"teacher_{i}" for i in range(groups_per_round)],
    [f"student_{i}" for i in range(2 * groups_per_round)],
]

matcher = create_typed_matcher(groups_per_round,
                               group_spec,
                               participant_labels=participant_labels)

```

```Python
>>> print(matcher.participant_types)
[['teacher_0', 'teacher_1', 'teacher_2', 'teacher_3', 'teacher_4'], ['student_0', 'student_1', 'student_2', 'student_3', 'student_4', 'student_5', 'student_6', 'student_7', 'student_8', 'student_9']]
>>> print(matcher.groups_for_next_round())
[['teacher_0', 'student_0', 'student_1'], ['teacher_1', 'student_2', 'student_3'], ['teacher_2', 'student_4', 'student_5'], ['teacher_3', 'student_6', 'student_7'], ['teacher_4', 'student_8', 'student_9']]
```
