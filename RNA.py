#!/usr/bin/env python
import sys

dna = open(sys.argv[1]).read().strip()
dna.replace("T", "U")