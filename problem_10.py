#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
Number = 2000000

if __name__ == "__main__":
	print(
		functools.reduce(
			operator.add,
			eratosthenes_sieve(Number)
			)
		)