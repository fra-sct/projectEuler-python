#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Self powers
# Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
Max = 1000
#Answer = 9110846700

if __name__ == "__main__":
	print(
		str(
			sum(
				map(
					lambda i: i**i,
					range(1, Max + 1)
					)
				)
			)[-10:]
		)