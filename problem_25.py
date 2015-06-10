#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# 1000-digit Fibonacci number
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#	Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#	F1 = 1
#	F2 = 1
#	F3 = 2
#	F4 = 3
#	F5 = 5
#	F6 = 8
#	F7 = 13
#	F8 = 21
#	F9 = 34
#	F10 = 55
#	F11 = 89
#	F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?
Target = 1000

if __name__ == "__main__":
	for i in itertools.count(1):
		if len(str(fibonacci(i))) == Target:
			print(i)
			break