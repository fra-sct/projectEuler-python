#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys
if sys.version_info.major < 3:
	input = raw_input
from lib import *
# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
#    *	1 Jan 1900 was a Monday.
#    *	Thirty days has September,
#    	April, June and November.
#  	 	All the rest have thirty-one,
#    	Saving February alone,
#    	Which has twenty-eight, rain or shine.
#    	And on leap years, twenty-nine.
#    *	A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
Year_Start = 1901
Year_End = 2000
#Answer=171

if __name__ == "__main__":
	print(
		list(
			filter(
				lambda i: i == 0,
				(get_weekday(1, month, year)
					for year in range(Year_Start, Year_End+1)
					for month in range(1, 12+1)
					)
				)
			).count(0)
		)