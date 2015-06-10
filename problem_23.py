#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Range = 28123
#Answer = 4179871

def is_perfect(n):
	return sum(proper_divisors(n)) == n

def is_deficient(n):
	return sum(proper_divisors(n)) < n

def is_abundant(n):
	return sum(proper_divisors(n)) > n

#Well, I can filter out all the non-abundant numbers out of the range(1, 28123), and then subtract the sum of all the permutations of the sum of all abundant numbers from the the sum of all the numbers 1..28123.

if __name__ == "__main__":
	abundant_numbers = list(
		filter(
			is_abundant,
			range(1, Range)
			)
		)
	are_composite = set(
		i + j
		for i in abundant_numbers
		for j in abundant_numbers
		)
	print(
#		sum_naturals(Range) - 
		sum(
			filter(
				lambda n: n not in are_composite,
				range(Range)
				)
			)
		)