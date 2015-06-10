#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Highly divisible triangular number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
Target = 500 #divisors
#Answer: 76576500

if __name__ == "__main__":
	for i in itertools.count(start=1):
		_number = triangular(i)
		_divisors = divisors(_number)
		if len(_divisors) >= Target:
			print(_number)
			break
		#elif len(_divisors) % 5 == 0 and len(_divisors) > 50:
		#	print(_number, len(_divisors))
	# print(
		
		# )
	# print(
		# list(map(lambda i: (len(factorize(i)), i, factorize(i))[0],
		# filter(
			# lambda i: len(factorize(i)) == 5,
		# itertools.takewhile(
			# lambda i: len(factorize(i)) <= 5,
			# map(
				# triangular,
				# itertools.count(start=1)
				# )
			# )
			# )
			# )
		# ))