#!/usr/bin/env python
import sys

dna = open(sys.argv[1]).read().strip()
print " ".join(str(dna.count(x)) for x in "ACGT")