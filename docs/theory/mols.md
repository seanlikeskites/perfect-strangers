---
title: MOLS
---

# Mutually Orthogonal Latin Squares 
## Latin Squares
A Latin square of order $n$ is an $n{\times}n$ matrix with elements taken from a set of $n$ symbols such that each symbol
occurs exactly once in each row and column. The following figure gives an example of a Latin square of order 4 on the set of
symbols $\{0, 1, 2, 3\}$.

![Latin Square 1](../diagrams/mols/ls1.svg)
/// caption
A Latin Square of Order 4
///

## Orthogonal Latin Squares
Two Latin squares of order $n$ are said to be orthogonal if the ordered pairs of symbols formed by taking the elements at
the same position in each square are all distinct. Because there are $n^{2}$ such pairs, they constitute all possible
ordered pairs whose first element comes from the symbol set of the first square and whose second element comes from the
symbol set of the second square.

Below is an example of a pair of orthogonal Latin squares of order 4.

<div style="display: flex; justify-content: center;">
  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Latin Square 2" src="../diagrams/mols/ls2.svg"></p>
    </figure>
  </div>

  <div style="width: 30%">
    <figure markdown="span">
      <p><img alt="Latin Square 3" src="../diagrams/mols/ls3.svg"></p>
    </figure>
  </div>
</div>

Superimposing these squares gives the ordered pairs of elements shown below. These pairs constitute every ordered pair of
symbols in the set $\{0, 1, 2, 3\}$.

![Overlayed Latin Square](../diagrams/mols/overlayed_squares.svg)
/// caption
Superimposed Orthogonal Latin Squares
///

## Mutually Orthogonal Latin Squares
A set of Latin squares of the same order are said to be mutually orthogonal if every pair of squares from the set is
orthogonal. Mutually orthogonal Latin squares $\left(\mathrm{MOLS}\right)$ are closely related to [transversal
designs](./block_designs#transversal-designs).

The number of $\mathrm{MOLS}$ of a given order $n$ is at most $n - 1$. The three Latin squares of order 4 shown above
constitute a complete set of $4 - 1 = 3$ $\mathrm{MOLS}$. A complete set of $n - 1$ $\mathrm{MOLS}$ is not always possible however. For
example, it is known there are no orthogonal Latin squares of order 6.
