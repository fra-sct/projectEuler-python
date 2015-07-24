#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 9,
        name = "Special Pythagorean triplet",
        description = \
""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
        )

def is_pythagorean_triplet(a, b, c):
	if not (a < b < c):
		return False
	if a**2 + b**2 == c**2:
		return True
	return False

def complete_triplet(a, b):
	return is_pythagorean_triplet(a, b, int((a**2+b**2)**0.5))

with setup(problem):
	#First, I generate all possible triplets
	Numbers = (
		(a, b, int((a**2 + b**2)**0.5)) 
		for a in range(1, 1000)
		for b in range(1, 1000)
		if complete_triplet(a, b) 
		)
	#Then, I filter out all the values such as a+b+c!=1000
	Numbers = filter(
		lambda i: i[0] + i[1] + i[2] == 1000,
		Numbers
		)
	problem.answer = list(
                map(
                        lambda i: functools.reduce(operator.mul, i),
                        Numbers
                )
        )[0]
