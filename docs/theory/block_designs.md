# Block Designs
## Introduction
Solutions to the perfect stranger matching problem take the form of block designs. These are combinatorial structures made
up of a set of "points" $X$ and a family of "blocks" (subsets of $X$) which satisfy some constraints. In their application
to perfect stranger matching $X$ would be the set of all participants and the blocks the groups these participants are
placed in. In the following discussion the following terms refer to these elements of an experiment:

  * Points -> Participants
  * Blocks -> Groups
  * Block Size -> Group Size $\beta$

Under perfect stranger matching conditions, the following principles determine what types of block designs can be used:

  * Any pair of participants appear in the same group together at most once.
  * Every participant should participate in every round.

The first of these can be ensured by choosing block designs where any two blocks intersect at at most one point. To ensure
the second, the block design must be resolvable.

### Resolvable Block Designs
A resolvable block design is one in which the blocks can be grouped into "parallel classes" where each parallel class
contains every point in $X$ exactly once. In such a design the blocks of a given parallel class give the groups for a single
round of the experiment:

  * Parallel Class -> Round

Designing an experiment with the largest number of rounds is then equivalent to finding a block design with the greatest
number of parallel classes.

## Balanced Incomplete Block Designs (BIBDs)
A balanced incomplete block design (BIBD) has parameters: $v$, $k$, and $\lambda$. Given a set $X$ of $v$ points, the design
consists of blocks of $k$ points such that each unordered pair of points from $X$ appears in exactly $\lambda$ blocks. A
BIBD for a given set of parameters is referred to as a ($v$, $k$, $\lambda$)-design.

For perfect stranger matching applications we consider resolvable BIBDs for which:

  * $v = \alpha\beta$
  * $k = \beta$
  * $\lambda = 1$

Setting $\lambda = 1$ ensures perfect stranger matching. If a resolvable ($\alpha\beta$, $\beta$, 1)-design exists for the
given experiment parameters, every participant will meet every other participant exactly once if all possible rounds are
conducted. The maximum number of rounds is therefore equal to the [trivial upper bound](overview#trivial-upper-bound).

For a resolvable ($v$, $k$, 1)-design to exist, $v$ must be divisible by $k$ and $v - 1$ must be divisible by $k - 1$. In
terms of experiment parameters that means that $\frac{\alpha\beta - 1}{\beta - 1}$ must be an integer. This does not
guarantee existence of the design however, for example a (36, 6, 1)-design does not exist.

A class of easily constructible resolvable BIBDs are the [finite affine planes](finite_planes). A resolvable ($k^{2}$, $k$,
1)-design exists whenever the finite affine plane of order $k$ exists.
