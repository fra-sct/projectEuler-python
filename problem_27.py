#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 27,
	name = "Quadratic primes",
	description = \
"""Euler discovered the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| < 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""	)
Range = 1000
#Answer: -59231 (n^2 + -61 + 971, 71 consecutive primes) (0:00:35.723)

with setup(problem):
	#Oh well. If I cannot be clever, well, then let's be brutal. It's only
	# four millions possible combinations. Well, just over half a minute.
	#And if I wanted to be clever?W
	Polynomials = []#(a, b, len)
	for a in range(-Range, +Range):
		if not is_prime(abs(a)): continue
		for b in range(-Range, +Range):
			p = lambda n: n**2 + a*n + b
			l = len(
				list(
					itertools.takewhile(
						lambda n: n>0 and is_prime(n),
						map(
							p,
							itertools.count(0)
							)
						)
					)
				)
			if l:
				Polynomials.append((a, b, l))
	a, b, l = max(Polynomials, key=lambda i: i[2])
	problem.answer = "{0} (n^2 + {1} + {2}, {3} consecutive primes)".format(
		a * b, a, b, l)