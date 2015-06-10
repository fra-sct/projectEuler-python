#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

if __name__ == "__main__":
	products = (
			i * j 
			for i in range(100, 1000)
			for j in range(100, 1000)
		)
	print(
		max(
			filter(
				palindrome,
				products
				)
			)
		)