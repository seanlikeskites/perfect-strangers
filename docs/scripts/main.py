# Create HTML table of maximum sequence lengths for various combinations of parameters
# and compare to results given by Both et al. (2016).
from perfect_strangers import create_matcher
from perfect_strangers.column_shift_matcher import ColumnShiftMatcher
from perfect_strangers.finite_plane_matcher import FinitePlaneMatcher
from perfect_strangers.kirkman_triple_matcher import KirkmanTripleMatcher
from perfect_strangers.lookup_matcher import LookupMatcher
from perfect_strangers.nearly_kirkman_triple_matcher import NearlyKirkmanTripleMatcher
from perfect_strangers.round_robin_matcher import RoundRobinMatcher
from perfect_strangers.sub_bibd_matcher import SubBIBDMatcher
from perfect_strangers.util import sequence_length_upper_bound


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
    groups_per_round = row[0]["groups_per_round"]
    header_cell = f"<th>{groups_per_round}</th>"

    return header_cell + "".join([format_cell(c) for c in row])


def format_first_row(row, num_rows):
    return f'<tr><th rowspan="{num_rows}" class="vertical-title"><div>Groups per Round</div></th>' + format_row(row) + "</tr>"


def format_other_row(row):
    return "<tr>" + format_row(row) + "</tr>"


def create_table_body(data):
    return "<tbody>" + format_first_row(data[0], len(data)) + "".join([format_other_row(r) for r in data[1:]]) + "</tbody>"


def create_table_head(data):
    labels = f'<tr><th colspan="2"/><th colspan="{len(data[0])}">Group Size</th></tr>'

    group_sizes = '<tr><th colspan="2"/>' + "".join([f'<th>{c["group_size"]}</th>' for c in data[0]]) + "</tr>"

    return "<thead>" + labels + group_sizes + "</thead>"


def create_table(data):
    return '<table class="data-table">' + create_table_head(data) + create_table_body(data) + "</table>"


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
                "groups_per_round": groups_per_round,
                "group_size": group_size,
                "sequence_length": m.max_rounds,
                "method": type(m),
                "uses_lookup": type(m) is LookupMatcher,
                "meets_benchmark": benchmark is not None and m.max_rounds >= benchmark.max_rounds and type(m) is not LookupMatcher,
                "is_upper_bound": m.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)
            })

        sequence_lengths.append(row)

    return create_table(sequence_lengths)

def define_env(env):
    env.variables["benchmark_table"] = create_benchmark_table()
