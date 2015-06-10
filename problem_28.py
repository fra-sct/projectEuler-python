#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#Max = 1001 * 1001
Side = 1001
#Answer = 669171001

#Ok, explanation time.
#Look at the spiral: you start with an 1, then 3, 5, 7, 9, then
# 13, 17, 21, 25.
#Or, you increase the current number by 2*j each time, where j is
# the distance of the current number from the center.
#j itself increases by 1 every 4 numbers.

if __name__ == "__main__":
	Sum = 1
	i, j, k = 1, 0, 3
	while i < (Side * Side):
		k += 1
		if k > 3:
			j, k = j+1, 0
		i += j * 2
		Sum += i
	print(Sum)