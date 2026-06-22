# Overview
The aim of perfect stranger matching is to generate a sequence of participant groupings such that over the course of a multi
round experiment no two participants are placed in the same group more than once (i.e. in every round participants are placed
in a group of participants they have not been grouped with in previous rounds). 

Finding the longest possible sequence which satisfies these criteria is a computationally complex problem in the field of
combinatorial design. This document provides some basic analysis of this problem and an introduction to some of the
algorithms used to tackle it.

## Experiment Parameters
The two parameters which determine how participants are grouped in an experiment are as follows:

  * $\alpha$: The number of groups in each round of the experiment.
  * $\beta$: The number of participants per group.

This gives a total of $\alpha\beta$ participants. To identify individual participants we enumerate them starting at $0$ up
to $\alpha\beta - 1$.

## Grouping Matrices
The groupings for each round of an experiment are defined by a $\alpha{\times}\beta$ matrix. Each row of this matrix
represents a group of participants. For example, the following matrix defines 4 groups of 3 participants.


$$
    \mathbf{G} = \begin{bmatrix}
        0 & 1 & 2 \\
        3 & 4 & 5 \\
        6 & 7 & 8 \\
        9 & 10 & 11
    \end{bmatrix}
$$

In an $n$ round experiment we'd have a sequence of such grouping matrices which satisfies the perfect stranger matching
criteria:

$$
    \mathbf{G}^{(0)}, \mathbf{G}^{(1)}, \dots, \mathbf{G}^{(n - 1)}
$$


## Maximum Sequence Length
Given the above parameters, we denote the maximum number of rounds possible under the perfect stranger matching criteria as
$l_{\max}(\alpha, \beta)$.

### Trivial Upper Bound
A trivial upper bound on the maximum sequence length can be found by considering the maximum number of groups a single
participant can be a part of before meeting another participant for a second time. For each participant there are
$\alpha\beta − 1$ other participants they could be matched with at some point in the experiment. Each round each participant
must be matched with $\alpha − 1$ participants from this list to form a group. This gives us the following upper bound for
the maximum sequence length.

$$
	l_{\max}(\alpha, \beta) \leq \left\lfloor\frac{\alpha\beta - 1}{\beta - 1}\right\rfloor
$$

### When $\alpha < \beta$
If the number of groups per round is less than the number of participants in a group, only a single round is possible. In
attempting to construct groups for a second round, each group must contain at most 1 participant from each group in the
first round. As there are fewer groups than participants needed, this is not possible.

$$
	l_{\max}(\alpha, \beta) = 1, \quad \text{if} ~ \alpha < \beta
$$

## Algorithms
### Optimal Solutions
For some specific groups sizes there are known optimal solutions to the perfect stranger matching problem:

  * When $\beta = 2$ $~$---$~$ [Round Robin Matching](./round_robin.md)
  * When $\beta = 3$ $~$---$~$ Kirkman Triple Matching

### Generic Algorithms
Where no optimal solution is known we must rely on algorithmic methods to construct sequences of grouping matrices. The
perfect-strangers package aims to avoid search based algorithms. At present the package implements a [column shift
matching](./column_shift) approach.
