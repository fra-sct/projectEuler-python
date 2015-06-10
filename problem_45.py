#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Triangular, pentagonal, and hexagonal
# Problem 45
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.
#Fuck smart. I'll brute force the shit out of this.
Start = 40755
#Answer = 1533776805 #Bruteforced
Max = 100000

if __name__ == "__main__":
	triangle = lambda n: n * (n + 1) // 2
	pentagonal = lambda n: n * (3*n - 1) // 2
	hexagonal = lambda n: n * (2*n - 1)
	Triangulars = set(
		map(
			triangle,
			range(Max)
			)
		)
	Pentagonals = set(
		map(
			pentagonal,
			range(Max)
			)
		)
	Hexagonals = set(
		map(
			hexagonal,
			range(Max)
			)
		)
	for n in Triangulars:
		if n in Pentagonals and n in Hexagonals:
			print(n)