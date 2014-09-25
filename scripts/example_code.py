#!/usr/bin/env python
import itertools
# itertools.combinations('abcd',2)
# 	# itertools.combinations object at 0x01348F30>
# list(itertools.combinations('abcd',2))
# 	# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
# [''.join(x) for x in itertools.combinations('abcd',2)]
	# ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']

# More intertools info: https://docs.python.org/2/library/itertools.html




import operator as op

def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom