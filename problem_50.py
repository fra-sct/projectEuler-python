#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
Lower_Range, Upper_Range = 1000, 1000000
#Answer = 997651 #Length 543
#Lower_Range, Upper_Range = 1, 100
#Answer = 41 #Length 6

if __name__ == "__main__":
	Primes = eratosthenes_sieve(Upper_Range)
	Consecutive_Sums = [] #(sum, length)
	for i, prime in enumerate(Primes):
		sum, length = 0, 0
		for j in Primes[i:]:
			if sum + j >= Upper_Range: break
			sum += j
			length += 1
			Consecutive_Sums.append((length, sum))
	print(
		max(
			filter(
				lambda i: is_prime(i[1]),
				Consecutive_Sums
				)
			)
		)