#!/usr/bin/env python
import sys

id_dna_list = []
with open(sys.argv[1]) as data:
    def cg_percentage(dna):
        return (dna.count("C") + dna.count("G")) / float(len(dna))

    for line in data:
        line = line.rstrip()
        if line[0] == ">":
            id_dna_list.append([line[1::], ""])
        else:
            id_dna_list[-1][-1] += line

id_cg_percentage_list = map(lambda x: (x[0], cg_percentage(x[1])), id_dna_list)
max_data = max(id_cg_percentage_list, key=lambda x: x[1])

print max_data[0] + "\n" + str(max_data[1] * 100) + "%"