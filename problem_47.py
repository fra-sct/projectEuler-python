#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 47,
	name = "Distinct primes factors",
	description = \
"""The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2^2 × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?"""
	)
Lower_Range = 210 #2*3*5*7
Consecutive_Factors = 4

with setup(problem):
	x = 0
	for n in itertools.count(Lower_Range):
		if len(set(factorize(n))) == Consecutive_Factors:
			x += 1
			if x == Consecutive_Factors:
				problem.answer = n - (Consecutive_Factors - 1)
				break
		else: x = 0