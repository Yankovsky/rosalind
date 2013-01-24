#!/usr/bin/env python
from string import maketrans
import sys

dna = open(sys.argv[1]).read().strip()
print dna[::-1].translate(maketrans("ATCG", "TAGC"))