#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 5,
        name = "Smallest multiple",
        description = \
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
)

with setup(problem):
	problem.answer = lcm(
                *list(range(1, 20 + 1))
        )
