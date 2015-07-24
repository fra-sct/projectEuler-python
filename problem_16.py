#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 16,
        name = "Power digit sum",
        description = \
"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?"""
        )
Base = 2
Exponent = 1000

with setup(problem):
	problem.answer = sum(
                map(
                        int,
                        str(
                                Base ** Exponent
                        )
                )
        )
