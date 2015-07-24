#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 4,
        name = "Largest palindrome product",
        description = \
"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
        )

with setup(problem):
	products = (
			i * j 
			for i in range(100, 1000)
			for j in range(100, 1000)
		)
	problem.answer = max(
                filter(
                        palindrome,
                        products
                )
        )
