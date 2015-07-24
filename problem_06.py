#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 6,
        name = "Sum square difference",
        description = \
"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
        )
Top_Range = 100 + 1

with setup(problem):
	sum_squares, sum = 0, 0
	for n in range(1, Top_Range):
		sum_squares += n ** 2
		sum += n
	square_sum = sum ** 2
	
	problem.answer = abs(sum_squares - square_sum)
