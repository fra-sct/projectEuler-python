#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 7,
        name = "10001st prime",
        description = \
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
        )
N = 10001 - 1 #I consider 2 to be the 0th prime number

with setup(problem):
	problem.answer = prime(N)
