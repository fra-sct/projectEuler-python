#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 41,
	name = "Pandigital prime",
	description = \
	"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?"""
	)

Max = 987654321 #The maximum 9-pandigital number - used to set
                # an upper range for the sieve.
Upper_Range = 9
Lower_Range = 4
#Answer = 7652413 (in 3.169s - yay!)
#At first I got 1234657, as I forgot to check the numbers in reverse order...
#How I did it:
# 1. use eratosthenes sieve to generate all the primes up to
#    987654321 ** 0.5 (to check for primality)
# 2. generate all the pandigital numbers up to Upper_Range
# 3. filter the pandigital numbers with is_prime
# 4. ????
# 5. profit!

with setup(problem):
	Primes = eratosthenes_sieve(int(Max ** 0.5))
	for i in range(Upper_Range, Lower_Range, -1):
		for n in reversed(list(generate_pandigitals(i))):
			if any(n % p == 0 for p in Primes): continue
			problem.answer = n
			break	