# Round Robin Matching
When participants grouped in pairs each round, perfect stranger matching is equivalent to arranging a round robin
tournament in which every player meets every other player exactly once.

## Algorithm
The algorithm for round robin matching implemented in the perfect-strangers package is as follows. First construct the
grouping matrix for the first round, $\mathbf{G}^{(0)}$, using any pairing strategy, for example:


![Grouping Matrix](../diagrams/round_robin/initial.svg)
/// caption
///

Then pick an element of the matrix to fix in place. In this example we use the top left element.


![Fixed Element](../diagrams/round_robin/fixed.svg)
/// caption
///

For each subsequent round, rotate the elements of the matrix (either clockwise or anti-clockwise) one position, keeping the
fixed element in place.

![Fixed Element](../diagrams/round_robin/rotated.svg)
/// caption
///

Repeated rotation like this will cycle through every possible set of pairings for the participants.

### Eliminating Bias
One issue with this algorithm is that participants will meet other participants in the same order as each other. In
experiments which this might introduce bias, it is sufficient to generate all grouping matrices ahead of time and randomise
their order.

