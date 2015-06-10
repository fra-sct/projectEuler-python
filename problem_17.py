#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
Target = 1000
#Answer=21124

if __name__ == "__main__":
	print(
		sum(
			map(
				len,
				map(
					lambda i: i.replace(' ', '').replace('-', ''),
					map(
						to_words,
						range(1, Target + 1)
						)
					)
				)
			)
		)