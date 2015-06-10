#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
Target = 1000000
#Answer = 55

def is_circular(n, seq):
	return all(
		map(
			lambda i: i in seq,
			rotations(n)
			)
		)

def rotate(n):
	t = str(n)
	return int(t[-1] + t[:-1])

def rotations(n):
	return list(
		itertools.accumulate(
			[n] * len(str(n)),
			lambda i, j: rotate(i)
			)
		)
	
if __name__ == "__main__":
	Primes = set(
		eratosthenes_sieve(Target)
		)
	print(
		len(
			list(
				filter(
					lambda i: is_circular(i, Primes),
					Primes
					)
				)
			)
		)