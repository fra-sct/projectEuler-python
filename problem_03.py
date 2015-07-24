#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 3,
        name = "Largest prime factor",
        description = \
"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""
        )
Number = 600851475143

with setup(problem):
	problem.answer = max(
                factorize(Number)
        )
