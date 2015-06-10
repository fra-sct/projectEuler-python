#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 46,
	name = "Goldbach's other conjecture",
	description = \
"""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
    9 = 7 + 2*1^2
    15 = 7 + 2*2^2
    21 = 3 + 2*3^2
    25 = 7 + 2*3^2
    27 = 19 + 2*2^2
    33 = 31 + 2*1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""
	)

def satisfies_goldbach(n):
	for p in primes_upto(n):
		for i in range(1, int(n**0.5)):
			if p + 2*i**2 == n:
				return True
	return False

with setup(problem):
	primes_upto(1000)
	for n in itertools.count(3, 2):
		if is_prime(n): continue
		if not satisfies_goldbach(n):
			problem.answer = n
			break