#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#    1634 = 14 + 64 + 34 + 44
#    8208 = 84 + 24 + 04 + 84
#    9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
Upper_Bound = (9**5) * 6
#Answer = 443839 #443840 #I forgot to remove the 1

def sum_of_fifth_powers(n):
	return sum(
		map(
			lambda i: i**5,
			map(
				int,
				str(n)
				)
			)
		)

if __name__ == "__main__":
	print(
		sum(
			filter(
				lambda i: sum_of_fifth_powers(i) == i,
				range(2, Upper_Bound)
				)
			)
		)