import pandas as pd
from tabulate import tabulate

from perfect_strangers import create_matcher

l = pd.DataFrame([], index=range(2, 31), columns=range(2, 7))


for groups_per_round in l.index:
    for group_size in l.columns:
        m = create_matcher(groups_per_round, group_size)

        l.loc[groups_per_round, group_size] = m.max_rounds

t = l - l
t.loc[2] = [3, 1, 1, 1, 1]
t.loc[3] = [5, 4, 1, 1, 1]
t.loc[4] = [7, 4, 5, 1, 1]
t.loc[5] = [9, 7, 5, 6, 1]
t.loc[6] = [11, 8, 6, 6, 3]
t.loc[7] = [13, 9, 7, 5, 0]
t.loc[8] = [15, 10, 8, 6, 0]
t.loc[9] = [17, 11, 9, 0, 0]
t.loc[10] = [19, 13, 10, 0, 0]
t.loc[11] = [21, 14, 0, 0, 0]
t.loc[12] = [23, 15, 0, 0, 0]
t.loc[13] = [25, 17, 0, 0, 0]

print(tabulate(l, headers="keys", tablefmt="psql"))
print(tabulate(l - t, headers="keys", tablefmt="psql"))


