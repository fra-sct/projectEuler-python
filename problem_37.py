#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#Answer = 748317

r_trunc = lambda n, i: int(str(n)[:-i])
l_trunc = lambda n, i: int(str(n)[i:])

def is_truncatable(n, seq):
	return n not in (2, 3, 5, 7) and all(
		r_trunc(n, i) in seq and l_trunc(n, i) in seq
		for i in range(1, len(str(n)))
		)

if __name__ == "__main__":
	Primes = set(
		eratosthenes_sieve(1000000)#Limit found by good old T&E
		)
	print(
		sum(
			list(
				filter(
					lambda i: is_truncatable(i, Primes),
					Primes
					)
				)
			)
		)