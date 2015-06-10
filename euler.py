#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import sys, atexit, textwrap
from lib import *
from time import clock
from contextlib import contextmanager

Width = 79#60

class Problem(object):
	def __init__(self, id, name, description = ""):
		self.name, self.id, self.description = \
			name, id, description
		self.answer = None
	def __str__(self):
		s = "Problem {0} - {1}".format(
			self.id,
			self.name)
		if len(self.description) > 0:
			for line in self.description.split('\n'):
				s += '\n'
				s += '\n'.join(
					textwrap.wrap(
						line,
						width = Width
						)
					)
		return s

@contextmanager
def setup(p):
	global start
	print(p)
	start = clock()
	yield
	endlog()
	print("Answer: {0}".format(p.answer))

#The following section is by Paul McGuire
#http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution/1557906#1557906

def seconds_to_str(t):
	return "%d:%02d:%02d.%03d" % \
		functools.reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
			[(t*1000,),1000,60,60])

line = "=" * Width
def log(s, elapsed=None):
	print(line)
	print(seconds_to_str(clock()), '-', s)
	if elapsed:
		print("Elapsed time:", elapsed)
	print(line)
	print

def endlog():
	end = clock()
	elapsed = end-start
	log("End Program", seconds_to_str(elapsed))

def now():
	return seconds_to_str(clock())

#print_metadata()
#log("Start Program")