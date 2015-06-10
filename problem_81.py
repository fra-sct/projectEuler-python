#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Path sum: two ways
# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
# [131, 673, 234, 103, 18],
# [201, 96, 342, 965, 150],
# [630, 803, 746, 422, 111],
# [537, 699, 497, 121, 956],
# [805, 732, 524, 37, 331]
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
Filename = "p081_matrix.txt"
#Answer = 427337
Matrix = [
	[131, 673, 234, 103, 18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331]
]
Bottom_Right = b_x, b_y = len(Matrix[-1]) - 1, len(Matrix) - 1

if __name__ == "__main__":
	Matrix = list(
		map(
			lambda i: list(map(int, i)),
			map(
				lambda i: i.strip().split(","),
				open(Filename).readlines()
				)
			)
		)
	Bottom_Right = b_x, b_y = len(Matrix[-1]) - 1, len(Matrix) - 1
	for i, line in enumerate(Matrix):
		for j, cell in enumerate(line):
			#What follows is quite silly and inelegant
			#There is a better way to enumerate the adjacents,
			# I just know it...
			adjacents = []
			if i > 0: adjacents.append(Matrix[i-1][j])
			if j > 0: adjacents.append(Matrix[i][j-1])
			if len(adjacents) == 0: adjacents = [0]
			Matrix[i][j] += min(adjacents)
	print(Matrix[b_y][b_x])