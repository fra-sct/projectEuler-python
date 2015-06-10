#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
Upper_Range = 1000000
#Answer = 872187

if __name__ == "__main__":
	print(
		sum(
			filter(
				lambda i: palindrome(i) and palindrome("{0:b}".format(i)),
				range(Upper_Range)
				)
			)
		)