#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 10,
        name = "Summation of primes",
        description = \
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""
        )
Number = 2000000

with setup(problem):
	problem.answer = functools.reduce(
                operator.add,
                eratosthenes_sieve(Number)
        )
