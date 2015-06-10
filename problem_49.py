#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 49,
	name = "Prime permutations",
	description = \
"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""
	)
Digits = 4
Increase = 3330
#Answer: 296962999629

def filter_function(n):
	if not (is_prime(n + Increase) and is_prime(n + 2*Increase)):
		return False
	#print(n, sorted(str(n)), sorted(str(n +Increase)))
	return sorted(str(n)) == \
		sorted(str(n + Increase)) == \
		sorted(str(n + 2*Increase))

with setup(problem):
	problem.answer = list(
		filter(
			filter_function,
			filter(
				lambda n: (n // 1000) > 0,
				eratosthenes_sieve(10000)
				)
			)
		)
	problem.answer = (
		"{0}{1}{2} ({0}, {1}, {2})".format(n, n + Increase, n + 2*Increase)
		for n in problem.answer)
	problem.answer = "\n\t".join(problem.answer)
		