#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#     ======+      ===+--+      ===+--+
#     |  |  #      |  #  |      |  #  |
#     +--+--#      +--+==+      +--#--+
#     |  |  #      |  |  #      |  #  |
#     +--+--v      +--+--v      +--+==>
#            
#     #--+--+      #--+--+      #--+--+
#     #  |  |      #  |  |      #  |  |
#     +=====+      +==+--+      #--+--+
#     |  |  #      |  #  |      #  |  |
#     +--+--v      +--+==>      +=====>
# How many such routes are there through a 20×20 grid?
Grid = 20
#Answer=137846528820

if __name__ == "__main__":
	print(
		factorial(2 * Grid) //
		factorial(Grid)**2
		)