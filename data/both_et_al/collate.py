#!/usr/bin/env python3

import glob
import json

grouping_data = {}

def load_file(file):

    with open(file) as f:
        # Skip comment at top of file.
        next(f)

        matrices = [json.loads(line) for line in f]

    groups_per_round = len(matrices[0])
    group_size = len(matrices[0][0])

    if groups_per_round in grouping_data:
        grouping_data[groups_per_round][group_size] = matrices
    else:
        grouping_data[groups_per_round] = {
            group_size: matrices
        }

def main():
    for file in glob.glob("*.txt"):
        load_file(file)

    with open("both_et_al_groupings.json", "w") as f:
        f.write(json.dumps(grouping_data))

if __name__ == "__main__":
    main()
