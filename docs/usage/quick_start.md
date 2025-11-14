# Quick Start

```Python
from perfect_strangers import create_matcher
```

```Python
groups_per_round = 5
group_size = 3

matcher = create_matcher(groups_per_round, group_size)
```

```Python
groups = matcher.groups_for_next_round()
```

