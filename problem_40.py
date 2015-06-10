#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#   12345678901 2 3
# 0.12345678910_1_112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
Max = 1000000
#Answer = 210

if __name__ == "__main__":
	#Brute force approach
	Champernowne = "".join(
		str(n) for n in range(Max + 1)
		)
	d = lambda n: int(Champernowne[n])
	#print(d(1), d(2), d(11),d(12))
	print(
		d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
		)