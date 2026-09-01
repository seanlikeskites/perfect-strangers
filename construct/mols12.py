# Construct 5 MOLS of order 12 as per Johnson et al. (1961)

def diff(a, b, mods):
    """
    Perform a - b in the group defined as the cross product of multiple cyclic groups.
    """
    return tuple((a[i] - b[i]) % m for i, m in enumerate(mods))

# For MOLS of order 12 we use the group given by Z_{6} x Z_{2}.
mods = (6, 2)

# Enumerate each element of the group.
I = [(x, y) for y in range(mods[1]) for x in range(mods[0])]

points = {
    p: i
    for i, p in enumerate(I)
}

# Orthomorphisms taken from the paper.
orthos = [
    I,
    [(0, 0), (0, 1), (2, 1), (2, 0), (1, 1), (1, 0), (3, 1), (5, 1), (4, 0), (4, 1), (5, 0), (3, 0)],
    [(0, 0), (3, 0), (0, 1), (1, 0), (3, 1), (5, 1), (2, 0), (2, 1), (5, 0), (4, 0), (1, 1), (4, 1)],
    [(0, 0), (2, 1), (1, 0), (5, 1), (5, 0), (3, 1), (3, 0), (4, 1), (2, 0), (1, 1), (0, 1), (4, 0)],
    [(0, 0), (4, 0), (5, 1), (4, 1), (2, 0), (1, 1), (2, 1), (0, 1), (3, 1), (1, 0), (3, 0), (5, 0)]
]

# Construct MOLS.
squares = [
    [
        [points[diff(a, b, mods)] for b in I]
        for a in o
    ]
    for o in orthos
]

print(squares)
