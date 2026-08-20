# Overview
The perfect-strangers package performs [perfect stranger matching](#perfect-stranger-matching) for defining groups of
participants in an experiment. This is a computationally complex problem in the field of combinatorial design, meaning
search algorithms can run for very long times without finding a suitable solution. For this reason, perfect-strangers
focuses on explicit constructions of solutions. While these may not always be optimal, it is quick to check if a suitable
solution for a given set of experiment parameters is available.

This document provides some basic analysis of this problem and an introduction to some of the constructions used to form
solutions.

## Perfect Stranger Matching
The aim of perfect stranger matching is to generate a sequence of participant groupings such that over the course of a multi
round experiment no two participants are placed in the same group more than once (i.e. in every round participants are placed
in a group of participants they have not been grouped with in previous rounds). 

### Experiment Parameters
The two parameters which determine how participants are grouped in an experiment are as follows:

  * $\alpha$: The number of groups in each round of the experiment.
  * $\beta$: The number of participants per group.

This gives a total of $\alpha\beta$ participants. To identify individual participants we enumerate them starting at $0$ up
to $\alpha\beta - 1$.

### Grouping Matrices
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
    \mathbf{G}^{0}, \mathbf{G}^{1}, \dots, \mathbf{G}^{n - 1}
$$

### Maximum Sequence Length
Given the above parameters, we denote the maximum number of rounds possible under the perfect stranger matching criteria as
$l_{\max}(\alpha, \beta)$.

#### Trivial Upper Bound
A trivial upper bound on the maximum sequence length can be found by considering the maximum number of groups a single
participant can be a part of before meeting another participant for a second time. For each participant there are
$\alpha\beta − 1$ other participants they could be matched with at some point in the experiment. Each round each participant
must be matched with $\alpha − 1$ participants from this list to form a group. This gives us the following upper bound for
the maximum sequence length.

$$
	l_{\max}(\alpha, \beta) \leq \left\lfloor\frac{\alpha\beta - 1}{\beta - 1}\right\rfloor
$$

#### When $\alpha < \beta$
If the number of groups per round is less than the number of participants in a group, only a single round is possible. In
attempting to construct groups for a second round, each group must contain at most 1 participant from each group in the
first round. As there are fewer groups than participants needed, this is not possible.

$$
	l_{\max}(\alpha, \beta) = 1, \quad \text{if} ~ \alpha < \beta
$$

### Construction Methods
#### Optimal Solutions
For some specific groups sizes there are known optimal solutions to the perfect stranger matching problem:

  * When $\beta = 2$ $~$---$~$ [Round Robin Matching](./round_robin)
  * When $\beta = 3$ and $\alpha$ is odd $~$---$~$ [Kirkman Triple Matching](./kirkman)
  * When $\beta = 3$ and $\alpha$ is even $~$---$~$ [Nearly Kirkman Triple Matching](./nearly_kirkman) 

Other optimal construction methods apply to a variety of group sizes:

  * [Primitive Element Matching](./primitive_element)
  * [Sub-RBIBD Matching](./sub_bibd)

#### Generic Construction Methods
Where no optimal solution is known we must rely on generic construction methods to form sequences of grouping matrices. The
perfect-strangers package uses the following construction methods.

  * [Finite Affine Plane Matching](./finite_planes)
  * [Column Shift Matching](./column_shift)

## Typed Perfect Stranger Matching
Typed perfect stranger matching (as it's called in [z-Tree](https://www.ztree.uzh.ch/en.html)) has the same restrictions as
perfect stranger matching but includes an extra condition that each group must be composed of certain numbers of different
types of participant. It is assumed that the type of a given participant is the same across all rounds of an experiment.

### Experiment Parameters
In place of the perfect stranger matching group size parameter $\beta$, typed perfect stranger matching has a series of
parameters, each define the number of a particular type of participant in each group. Where $N$ is the number of different
participant types we have the following experiment parameters:

  * $\alpha$: The number of groups in each round of the experiment.
  * $\beta_{0},\beta_{1},\dots,\beta_{N - 1}$: The numbers of each type of participant in each group.

The number of participants in each group is then:

$$
    \sum_{n = 0}^{N - 1} \beta_{n}
$$

### Maximum Sequence Length
We denote the maximum typed perfect stranger matching sequence length for the given parameters as $l_{\max}(\alpha,
\beta_{0}, \beta_{1}, \dots, \beta_{N - 1})$. If there is only a single participant type, typed perfect stranger matching is
equivalent to perfect stranger matching and the bounds on the maximum sequence length are as
[above](#maximum-sequence-length). When the number of types of participants $N > 1$, things are different.

#### Upper Bound when $N > 1$
Consider an experiment where each group has $\beta_{n}$ of one type of participant and $\beta_{m}$ of another. A single
participant of the first type must match with $\beta_{m}$ of the second type in each round. As there are only
$\alpha\beta_{m}$ participants of the second type in total, only $\alpha$ rounds are possible before they would meet the same
participant again.

$$
    l_{\max}(\alpha, \beta_{0}, \beta_{1}, \dots, \beta_{N - 1}) \leq \alpha, \quad \text{if} ~ N > 1
$$

### Construction Methods
The [finite affine plane](./finite_planes) and [column shift](./column_shift) matching methods can be used for typed perfect
stranger matching by excluding rounds in which participants of the same type would be grouped together.
