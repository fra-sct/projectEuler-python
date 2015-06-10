#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 42,
	name = "Coded triangle numbers",
	description = \
"""The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?"""
	)
Filename = "p042_words.txt"
Max = 40 #t40 is 820, and even a 30-letters word can be at most 780.

def is_triangular(n):
	"""Returns whether the number n is a triangular number or not."""
	temp = int(math.sqrt(8*n+1))
	return temp*temp == 8*n+1

with setup(problem):
	problem.answer = len(
		list(
			filter(
				is_triangular,
				map(
					score_word,
						map(
						lambda i: i.strip('"'),
						open(Filename).readline().split(",")
						)
					)
				)
			)
		)
	