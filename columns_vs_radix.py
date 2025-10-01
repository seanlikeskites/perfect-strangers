from perfect_strangers import ColumnShiftMatcher
from perfect_strangers.radix_matcher import RadixMatcher

for s in range(3, 7):
    for e in range(2, 4):
        c = ColumnShiftMatcher(s**(e-1), s)
        r = RadixMatcher(s, e)
        print(f"{s}-{e}: Columns: {c.max_rounds} Radix {r.max_rounds}")

