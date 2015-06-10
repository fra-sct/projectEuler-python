#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
import functools, itertools, operator
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

is_multiple_of = lambda x: lambda y: (y % x) == 0
is_multiple_of_3_or_5 = lambda x: is_multiple_of(3)(x) or is_multiple_of(5)(x)

if __name__ == "__main__":
	print(
		functools.reduce(
			operator.add,
			filter(
				is_multiple_of_3_or_5,
				range(1, 1000)
			)
		)
	)
