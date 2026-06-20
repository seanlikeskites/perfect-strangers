# Create HTML table of maximum sequence lengths for various combinations of parameters
# and compare to results given by Both et al. (2016).
from perfect_strangers import create_matcher
from perfect_strangers.util import sequence_length_upper_bound

def format_cell(data):
    cell_class = ""

    if data["is_upper_bound"]:
        cell_class = "upper-bound-performance"
    elif data["meets_benchmark"]:
        cell_class = "benchmark-performance"

    return f'<td class="{cell_class}">{data["sequence_length"]}</td>'


def format_row(row):
    groups_per_round = row[0]["groups_per_round"]
    header_cell = f"<th>{groups_per_round}</th>"

    return header_cell + "".join([format_cell(c) for c in row])


def format_first_row(row, num_rows):
    return f'<tr><th rowspan="{num_rows}" class="vertical-title"><p>Groups per Round</p></th>' + format_row(row) + "</tr>"


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
    both_et_al = [
        [3, 1, 1, 1, 1],
        [5, 4, 1, 1, 1],
        [7, 4, 5, 1, 1],
        [9, 7, 5, 6, 1],
        [11, 8, 6, 6, 3],
        [13, 9, 7, 5, 0],
        [15, 10, 8, 6, 0],
        [17, 11, 9, 0, 0],
        [19, 13, 10, 0, 0],
        [21, 14, 0, 0, 0],
        [23, 15, 0, 0, 0],
        [25, 17, 0, 0, 0]
    ]

    num_groups_range = range(2, 14)
    group_size_range = range(2, 7)

    sequence_lengths = []

    for i, groups_per_round in enumerate(num_groups_range):
        row = []

        for j, group_size in enumerate(group_size_range):
            m = create_matcher(groups_per_round, group_size)
            is_upper_bound = m.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)

            row.append({
                "groups_per_round": groups_per_round,
                "group_size": group_size,
                "sequence_length": m.max_rounds,
                "meets_benchmark": m.max_rounds >= both_et_al[i][j],
                "is_upper_bound": m.max_rounds == sequence_length_upper_bound(groups_per_round, group_size)
            })

        sequence_lengths.append(row)

    return create_table(sequence_lengths)

def define_env(env):
    env.variables["benchmark_table"] = create_benchmark_table()
