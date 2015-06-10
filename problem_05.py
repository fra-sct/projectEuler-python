#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
from collections import defaultdict
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

if __name__ == "__main__":
	factors = defaultdict(lambda: 0)
	print(
		lcm(
			*list(range(1, 20 + 1))
			)
		)