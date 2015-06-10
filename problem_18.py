#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Maximum path sum I
# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#	   _3_
#	  _7_ 4
#	 2 _4_ 6
#	8 5 _9_ 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#
#				  75
#				 95 64
#				17 47 82
#			   18 35 87 10
#			  20 04 82 47 65
#			 19 01 23 75 03 34
#			88 02 77 73 07 63 67
#		   99 65 04 28 06 16 70 92
#		  41 41 26 56 83 40 80 70 33
#		 41 48 72 33 47 32 37 16 94 29
#		53 71 44 65 25 43 91 52 97 51 14
#	   70 11 33 28 77 73 17 78 39 68 17 57
#	  91 71 52 38 17 14 91 43 58 50 27 29 48
#	 63 66 04 68 89 53 67 30 73 16 69 87 40 31
#	04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
Triangle = [
	[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20, 4, 82, 47, 65],
	[19, 1, 23, 75, 3, 34],
	[88, 2, 77, 73, 7, 63, 67],
	[99, 65, 4, 28, 6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
# Triangle = [
	# [3],
	# [7, 4],
	# [2, 4, 6],
	# [8, 5, 9, 3]
# ]

# Position = row, column
# Adjacents = (row+1, column), (row+1, column+1)

# def find_path(triangle, position, max = 0):
	# line, column = position
	# adjacents = (line + 1, column), (line + 1, column + 1)
	# print(position)
	# if line >= len(triangle):
		# return max
	# max += triangle[line][column]
	# print(find_path(triangle, adjacents[0], max))
	# print(find_path(triangle, adjacents[1], max))
	
# _max_path = lambda triangle, line, column: triangle[line][column] + max(
	# triangle[line+1][column], triangle[line+1][column+1])

# def find_longest_path(triangle, position = (0, 0)):
	# line, column = position
	# if line >= len(triangle) - 1:
		# return maximum
	# map(
		# lambda triangle, line, column: triangle[line][column] + max(
			# triangle[line+1][column], triangle[line+1][column+1]),
		# )
	
def handle_rows(bottom, top):
	row = []
	for i in range(len(top)):
		row.append(
			top[i] + max(bottom[i], bottom[i+1])
			)
	return row

if __name__ == "__main__":
	print(
		max(
			functools.reduce(
				handle_rows,
				Triangle[::-1]
				)
			)
		)