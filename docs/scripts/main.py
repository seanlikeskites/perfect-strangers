# Create HTML table of maximum sequence lengths for various combinations of parameters
# and compare to results given by Both et al. (2016).
from perfect_strangers import create_matcher, create_typed_matcher
from perfect_strangers.matchers import (
    ColumnShiftMatcher,
    FinitePlaneMatcher,
    KirkmanTripleMatcher,
    LookupMatcher,
    NearlyKirkmanTripleMatcher,
    RoundRobinMatcher,
    SubBIBDMatcher,
)
from perfect_strangers.util import sequence_length_upper_bound, unique_integers_summing_to_n


def format_cell(data):
    cell_class = ""

    if data["is_upper_bound"]:
        cell_class = "upper-bound-performance"
    elif data["meets_benchmark"]:
        cell_class = "benchmark-performance"
    elif data["uses_lookup"]:
        cell_class = "uses-lookup"

    if data["method"] == RoundRobinMatcher:
        link = "./theory/round_robin"
    elif data["method"] == KirkmanTripleMatcher:
        link = "./theory/kirkman"
    elif data["method"] == NearlyKirkmanTripleMatcher:
        link = "./theory/nearly_kirkman"
    elif data["method"] == FinitePlaneMatcher:
        link = "./theory/finite_planes"
    elif data["method"] == SubBIBDMatcher:
        link = "./theory/sub_bibd"
    elif data["method"] == ColumnShiftMatcher:
        link = "./theory/column_shift"
    else:
        link = "https://doi.org/10.1016/j.econlet.2016.06.028"

    return f'<td class="{cell_class} benchmark-cell" onclick="location.href = \'{link}\';">{data["sequence_length"]}</td>'


def format_row(row):
    row_title = row[0]["row_title"]
    header_cell = f'<th class="row-title">{row_title}</th>'

    return header_cell + "".join([format_cell(c) for c in row])


def format_first_row(row, num_rows, left_title):
    return f'<tr><th rowspan="{num_rows}" class="vertical-title"><div>{left_title}</div></th>' + format_row(row) + "</tr>"


def format_other_row(row):
    return "<tr>" + format_row(row) + "</tr>"


def create_table_body(data, left_title):
    return "<tbody>" + format_first_row(data[0], len(data), left_title) + "".join([format_other_row(r) for r in data[1:]]) + "</tbody>"


def create_table_head(data, top_title):
    labels = f'<tr><th colspan="2"/><th class="horizontal-title" colspan="{min(6, len(data[0]))}">{top_title}</th></tr>'

    column_titles = '<tr><th class="static-spacer-head" colspan="2"/>' + "".join([f'<th>{c["column_title"]}</th>' for c in data[0]]) + "</tr>"

    return "<thead>" + labels + column_titles + "</thead>"


def create_table(data, top_title="Group Size", left_title="Groups per Round"):
    return '<table class="data-table">' + create_table_head(data, top_title) + create_table_body(data, left_title) + "</table>"


def create_benchmark_table():
    num_groups_range = range(2, 21)
    group_size_range = range(2, 7)

    sequence_lengths = []

    for groups_per_round in num_groups_range:
        row = []

        for group_size in group_size_range:
            m = create_matcher(groups_per_round, group_size)
            benchmark = LookupMatcher.create_matcher(groups_per_round, group_size)

            row.append({
                "row_title": groups_per_round,
                "column_title": group_size,
                "sequence_length": m.max_rounds,
                "method": type(m),
                "uses_lookup": type(m) is LookupMatcher,
                "meets_benchmark": benchmark is not None and m.max_rounds >= benchmark.max_rounds and type(m) is not LookupMatcher,
                "is_upper_bound": m.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)
                })

        sequence_lengths.append(row)

    return create_table(sequence_lengths)

def create_typed_benchmark_table():
    num_groups_range = range(2, 13)
    group_size_range = range(2, 6)

    group_specs = [
        spec
        for group_size in group_size_range
        for spec in unique_integers_summing_to_n(group_size) if len(spec) > 1
    ]

    sequence_lengths = []

    for group_spec in group_specs:
        row = []

        for groups_per_round in num_groups_range:
            m = create_typed_matcher(groups_per_round, group_spec)

            row.append({
                "row_title": str(group_spec),
                "column_title": groups_per_round,
                "sequence_length": m.max_rounds,
                "method": type(m),
                "uses_lookup": False,
                "meets_benchmark": False,
                "is_upper_bound": m.max_rounds == sequence_length_upper_bound(groups_per_round, group_spec)
            })

        sequence_lengths.append(row)

    return create_table(sequence_lengths, left_title="Group Specification", top_title="Groups per Round")

def define_env(env):
    env.variables["benchmark_table"] = create_benchmark_table()
    env.variables["typed_benchmark_table"] = create_typed_benchmark_table()
