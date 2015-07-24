#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
        id = 15,
        name = "Lattice paths",
        description = \
"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    ======+      ===+--+      ===+--+
    |  |  #      |  #  |      |  #  |
    +--+--#      +--+==+      +--#--+
    |  |  #      |  |  #      |  #  |
    +--+--v      +--+--v      +--+==>
           
    #--+--+      #--+--+      #--+--+
    #  |  |      #  |  |      #  |  |
    +=====+      +==+--+      #--+--+
    |  |  #      |  #  |      #  |  |
    +--+--v      +--+==>      +=====>
How many such routes are there through a 20×20 grid?"""
        )
Grid = 20
#Answer=137846528820

with setup(problem):
	problem.answer = factorial(2 * Grid) //	factorial(Grid)**2
