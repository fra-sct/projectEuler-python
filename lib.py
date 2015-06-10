#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import print_function, division
from __future__ import division
import functools, itertools, operator, math

is_even = lambda x: (x % 2) == 0

def is_perfect_square(n):
	"""Returns True if n is a perfect square; False otherwise."""
	if n < 0:
		return False
	test = int(n**(0.5))
	return test * test == n

def is_integer(n):
	"""Returns True if the number n is an integer number; False otherwise."""
	return round(n) == n

def palindrome(s):
	"""Returns True if the string (or number) s is a palindrome."""
	s = str(s)
	for i in range(len(s) // 2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

def gcd(*numbers):
	"""Returns the greatest common divisor of two or more numbers."""
	if len(numbers) > 2:
		return functools.reduce(gcd, numbers)
	a, b = max(numbers), min(numbers)
	if b == 0:
		return a
	return gcd(b, a % b)
	
def lcm(*numbers):
	"""Returns the least common multiple of two or more numbers."""
	return functools.reduce(
		lambda a, b: (a * b) // gcd(a, b),
		numbers
		)

_FIBONACCI = [0, 1]
def fibonacci(n):
	"""Returns the nth fibonacci number."""
	global _FIBONACCI
	for i in range(len(_FIBONACCI), n + 1):
		_FIBONACCI.append(_FIBONACCI[i - 1] + _FIBONACCI[i - 2])
	return _FIBONACCI[n]

def fibonacci_upto(n):
	"""Returns all fibonacci numbers small than n."""
	i, last = 0, 0
	while last < n:
		last = fibonacci(i)
		i += 1
		if last < n:
			yield last
		else:
			return

def fibonacci_first(n):
	"""Returns the first n fibonacci numbers."""
	for i in range(n):
		yield fibonacci(i)

_TRIANGULAR = [0]
def triangular(n):
	"""Returns the nth triangular number."""
	global _TRIANGULAR
	for i in range(len(_TRIANGULAR), n + 1):
		_TRIANGULAR.append(_TRIANGULAR[i - 1] + i)
	return _TRIANGULAR[n]

def triangulars_upto(n):
	"""Returns all triangular numbers small than n."""
	i, last = 0, 0
	while last < n:
		last = triangular(i)
		i += 1
		if last < n:
			yield last
		else:
			return

def triangulars_first(n):
	"""Returns the first n triangular numbers."""
	for i in range(n):
		yield triangular(i)

def is_triangular(n):
	"""Returns whether the number n is a triangular number or not."""
	return is_perfect_square(8*n + 1)

_PENTAGONAL = [0]
def pentagonal(n):
	"""Returns the nth pentagonal number."""
	global _PENTAGONAL
	for i in range(len(_PENTAGONAL), n + 1):
		_PENTAGONAL.append(
			i * (3*i - 1) // 2
		)
	return _PENTAGONAL[n]

def pentagonals_upto(n):
	"""Returns all pentagonal numbers small than n."""
	i, last = 0, 0
	while last < n:
		last = pentagonal(i)
		i += 1
		if last < n:
			yield last
		else:
			return

def pentagonals_first(n, start=0):
	"""Returns the first n pentagonal numbers."""
	for i in range(start, n):
		yield pentagonal(i)

def pentagonals(n=0):
	"""Yields all the pentagonal numbers, starting with the nth number."""
	for i in itertools.count(n):
		yield pentagonal(i)

def is_pentagonal(n):
	"""Returns whether the number n is a pentagonal number or not."""
	return is_integer((1 + (24*n + 1)**(0.5)) / 6)

_FACTORIAL = [1, 1]
def factorial(n):
	"""Returns the factorial of n."""
	global _FACTORIAL
	for i in range(len(_FACTORIAL), n + 1):
		_FACTORIAL.append(_FACTORIAL[i - 1] * i)
	return _FACTORIAL[n]

_PRIMES = [2, 3, 5, 7, 11, 13]
def prime(n):
	"""Returns the nth prime number."""
	global _PRIMES
	for i in range(len(_PRIMES), n + 1):
		_PRIMES.append(next_prime(_PRIMES[-1]))
	return _PRIMES[n]

def next_prime(n):
	"""Returns the first prime number following n."""
	candidate = n + 2
	while True:
		if is_prime(candidate):
			return candidate
		candidate += 2

def is_prime(n):
	"""Returns whether n is a prime number or not."""
	if n in _PRIMES: 
		return True
	upper_limit, i = math.sqrt(n), 0
	while prime(i) <= upper_limit:
		if n % _PRIMES[i] == 0:
			return False
		i += 1
	return True

def primes_upto(n):
	"""Returns all prime numbers smaller than n."""
	i, last = 0, 0
	while last < n:
		last = prime(i)
		i += 1
		if last < n:
			yield last
		else:
			return

def primes_first(n):
	"""Returns the first n prime numbers."""
	for i in range(n):
		yield prime(i)

def eratosthenes_sieve(n):
	"""Returns all the prime numbers smaller than n using the Eratostenes Sieve."""
	upper_limit = int(n**0.5)+1
	if upper_limit <= 4:
		return [2, 3]
	numbers = range(2, n)
	for p in eratosthenes_sieve(upper_limit):
		numbers = list(
			filter(
				lambda i: (i == p) or (i % p != 0),
				numbers
				)
			)
	return numbers

_FACTORS = {1: [1]}
def factorize(n):
	"""Returns the list of prime factors of the number n."""
	if n in _FACTORS: return _FACTORS[n]
	factors = []
	upper_limit = int(n ** 0.5) + 1
	for p in primes_upto(upper_limit):
		if p * p > n: break
		while n % p == 0:
			factors.append(p)
			n = n // p
	if n > 1: factors.append(n)
	_FACTORS[n] = factors
	return factors

def divisors(n):
	"""Returns the list of all the divisors of the number n."""
	divisors = set([1])
	factors = factorize(n)
	for i in range(1, len(factors)):
		combinations = map(
				lambda i: functools.reduce(operator.mul, i),
				itertools.combinations(factors, i)
				)
		for i in combinations:
			divisors.add(i)
	return divisors

def collatz(n):
	"""Return the Collatz sequence starting with the number n."""
	sequence = [n]
	while n != 1:
		if is_even(n):
			n = n // 2
		else:
			n = 3 * n + 1
		sequence.append(n)
	return sequence

def sum_naturals(n):
	"""Returns the sum of all the natural numbers up to and including n."""
	return n * (n + 1) // 2

_NUMBERS = {
	0: 'zero', 
	1: 'one', 
	2: 'two', 
	3: 'three', 
	4: 'four', 
	5: 'five', 
	6: 'six', 
	7: 'seven', 
	8: 'eight', 
	9: 'nine',
	10: 'ten', 
	11: 'eleven', 
	12: 'twelve', 
	13: 'thirteen', 
	14: 'fourteen', 
	15: 'fifteen', 
	16: 'sixteen', 
	17: 'seventeen', 
	18: 'eighteen', 
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	}
def to_words(number):
	"""Returns the number n written out in English words."""
	string = ""
	n = number
	thousands = n // 1000
	n -= thousands * 1000
	hundreds = n // 100
	n -= hundreds * 100
	decades = n // 10
	n -= decades * 10
	units = n
	#print(number)
	if thousands:
		#print("THOU")
		string += "%s thousand"%_NUMBERS[thousands]
		#print(string)
	if hundreds:
		#print("HUND")
		if thousands:
			string += " and "
		string += "%s hundred"%_NUMBERS[hundreds]
		#print(string)
	if decades == 1:
		units += 10
		decades = 0
	if decades:
		#print("DECA")
		if hundreds or thousands:
			string += " and "
		if decades > 1:
			string += "%s"%_NUMBERS[decades * 10]
		#print(string)
	if units:
		#print("UNIT")
		if not decades and (hundreds or thousands):
			string += " and "
		if decades:
			string += "-"
		string += _NUMBERS[units]
	return string

def is_leap_year(year):
	"""Returns whether the year passed as a parameter is a leap year or not."""
	return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
	
def year_length(year):
	"""Returns the length of the year passed as a parameter."""
	return 366 if is_leap_year(year) else 365

def month_length(month, year):
	return _MONTHS_LENGTH[month] + (1 if month == 2 and is_leap_year(year) else 0)

_MONTHS_LENGTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
_STARTING_YEAR = 1900
def get_day(day, month, year):
	"""Given a date in the format day, month, year, returns the number of days since the 1st January 1900."""
	_day = 0
	for _year in range(_STARTING_YEAR, year):
		_day += year_length(_year)
	for _month in range(1, month):
		_day += month_length(_month, year)
		# days += _MONTHS_LENGTH[month]
		# days += 1 if month == 2 and is_leap_year(year) else 0
	_day += day
	return _day

def get_weekday(day, month, year):
	"""Returns the day of the week of the date passed as parameter (Sunday is 0, Monday is 1)."""
	return get_day(day, month, year) % 7

def proper_divisors(n):
	"""Returns the list of proper divisors of n (numbers less than n which divide evenly into n)."""
	return list(
			filter(
				lambda i: i < n,
				divisors(n)
			)
		)

def are_amicable(a, b):
	"""Returns whether the numbers a and b are amicable or not (a and b are an amicable pair if a!=b, d(a)=b and d(b)=a, where d(n) is the sum of the proper divisors of n)."""
	return a != b \
		and sum(proper_divisors(a)) == b \
		and sum(proper_divisors(b)) == a

def is_pandigital(n):
	"""Returns whether n is a pandigital number or not.
	Algorithm taken from http://stackoverflow.com/questions/2484892/fastest-algorithm-to-check-if-a-number-is-pandigital, with some small alterations."""
	digits, count = 0, 0
	while n > 0:
		tmp = digits
		shift = (n % 10) - 1
		if shift < 0: 
			return False
		digits |= 1 << shift
		if tmp == digits:
			return False
		count += 1
		n //= 10
	return digits == (1 << count) - 1

def generate_pandigitals(n):
	"""Returns all the n-digits, n-pandigital numbers."""
	digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	if n == 1:
		return digits
	return map(
		lambda i: int(
			''.join(
				str(d) for d in i
				)
			),
		itertools.permutations(digits[:n])
		)

def score_word(word):
	return sum(
			map(
				lambda c: 1 + ord(c) - ord('a'),
				word.lower()
			)
		)

if __name__ == "__main__":
	print(list(fibonacci_first(20)))
	print(list(fibonacci_upto(100)))
	print(list(triangulars_first(20)))
	print(list(triangulars_upto(100)))
	print(list(primes_first(20)))
	print(list(primes_upto(100)))
	print(factorize(12))
	print(palindrome("ABBA"))
	print(palindrome("baba"))
	print(palindrome("amanaplanacanalpanama"))
	print(palindrome("atoyotasatoyota"))
	print(palindrome("As well as some non-palindromes."))
	print(gcd(30, 20, 10, 5), gcd(21,6,2))
	print(lcm(4,6), lcm(21, 6, 2), lcm(8,9,21))
	print(gcd(8, 9, 21))
	print(lcm(1,2,3,4,5,6,7,8,9,10))
	print(list(primes_upto(101)))
	#print(eratosthenes_sieve(10000))
	print(divisors(28))