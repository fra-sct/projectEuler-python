#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 43,
	name = "Sub-string divisibility",
	description = \
"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property."""
	)
#Answer: 16695334890 (found in 0:00:40.206)
#At first I forgot to include `== 0` in the lambda, and I got
# an absurdly long number. I was quite stumped for a while, as
# I distinctly remembered including that bloody `== 0` in that
# bloody lambda.

def generate_pandigitals():
	"""Returns all the 10-digits, 10-pandigital numbers, in string form."""
	digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	return filter(
		lambda i: i[0] != '0',
		map(
			lambda i: ''.join(
					str(d) for d in i
					),
			itertools.permutations(digits)
			)
		)


with setup(problem):
	problem.answer = sum(
			map(
				int,
				filter(
					lambda n: all(
						int(n[i:i+3]) % (0,2,3,5,7,11,13,17)[i] == 0
						for i in range(1,8)
						),
					generate_pandigitals()
					)
			)
		)