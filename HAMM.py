#!/usr/bin/env python
import sys

data = open(sys.argv[1]).read().strip()
dnas = data.split()
print sum(a != b for a, b in zip(dnas[0], dnas[1]))