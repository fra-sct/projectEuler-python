#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Power digit sum
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
Base = 2
Exponent = 1000

if __name__ == "__main__":
	print(
		sum(
			map(
				int,
				str(
					Base**Exponent
					)
				)
			)
		)