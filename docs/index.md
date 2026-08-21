---
render_macros: true
---

# perfect-strangers
Construction routines for perfect stranger matching in behavioural studies.

[Get Started](usage/quick_start.md){ .md-button .md-button--primary }

## Benchmarks
### Perfect Stranger Matching
Under [perfect stranger matching](theory/overview.md#perfect-stranger-matching) conditions, the maximum number of round
possible using this package for various combinations of experiment parameters is given in the following table.

<figure markdown="span">
  <div class="centre-table">
  {{ benchmark_table }}
  </div>
  <figcaption>Maximum Sequence Lengths for Perfect Stranger Matching</figcaption>
</figure>

Green cells indicate that this is a known optimal number of rounds. Orange cells indicate that a predefined set of groupings
is used as published by Both et al. (2016)[^1]. Blue cells indicate a construction approach which yields a number of rounds
greater than or equal to that given by Both et al. (2016). Clicking cells redirects to the documentation for the method used
to achieve each result.

### Typed Perfect Stranger Matching
Maximum numbers of rounds for various [typed perfect stranger matching](theory/overview.md#typed-perfect-stranger-matching)
configurations using this package are given below.

<figure markdown="span">
  <div class="centre-table">
    {{ typed_benchmark_table }}
  </div>
  <figcaption>Maximum Sequence Lengths for Typed Perfect Stranger Matching</figcaption>
</figure>

As above, green cells indicate that this is a known optimal number of rounds.

[^1]: Both, F., Adam, M.T.P., Hariharan, A., Dorner, V., Lux, E. and Weinhardt, C., 2016. A randomized tabu search-based
  approach for perfect stranger matching in economic experiments. Economics Letters, 145, pp.235-238. DOI:
  [10.1016/j.econlet.2016.06.028](https://doi.org/10.1016/j.econlet.2016.06.028)
