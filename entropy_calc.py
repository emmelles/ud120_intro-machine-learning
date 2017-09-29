#!/usr/bin/env python

import scipy.stats
import sys

def entropy(a,b):
    return scipy.stats.entropy([a,b],base=2)

# Notes to self: this normalises for convenience
a=float(sys.argv[1])
b=float(sys.argv[2])

print entropy(a,b)
