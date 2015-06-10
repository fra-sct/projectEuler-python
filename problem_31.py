#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
Target = 200
Coins = (1, 2, 5, 10, 20, 50, 100, 200)
Max_Coin = len(Coins) - 1

if __name__ == "__main__":
	Change = [1] + [0] * Target
	for i in range(0, Max_Coin + 1):
		for j in range(Coins[i], Target + 1):
			Change[j] += Change[j - Coins[i]]
	print(
		Change[Target]
		)