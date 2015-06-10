#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
Filename = "p022_names.txt"
#Answer = 871198282

if __name__ == "__main__":
	print(
		sum(
			itertools.starmap(
				lambda i, w: (i+1) * score_word(w),
				enumerate(
					sorted(
						map(
							lambda i: i.strip('"'),
							open(Filename).readline().split(",")
							)
						)
					)
				)
			)
		)