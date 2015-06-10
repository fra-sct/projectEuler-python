#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import *
problem = Problem(
	id = 59,
	name = "XOR decryption",
	description = \
"""Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text."""
	)
Filename = "p059_cipher.txt"

def xor_encrypt(key, file):
	# encrypted = []
	# i = 0
	# for byte in file:
		# encrypted.append(byte ^ key[i])
		# i = (i + 1) % len(key)
	# return encrypted
	return map(
		lambda b, k: b ^ k,
		file, itertools.cycle(key))

def score_text(text):
	import re
	score = 0
	for pattern in (
		"the", "an", "is", "are", "was", "were", "have", "has",
		"had", "one", "two", "three", "five", "six", "seven",
		"eight", "nine", "ten", "you", "he", "she", "it",
		"they", "my", "your", "his", "her", "its", "their"):
		found = re.findall(pattern, text, flags=re.I)
		score += len(found)
	return score

with setup(problem):
	chars = [n for n in range(ord('a'), ord('z')+1)]
	keys = list(itertools.product(chars, repeat=3))
	encrypted = list(map(int, open(Filename).read().split(',')))
	Key, Score, Decrypted = (0, 0, 0), -1, ""
	for key in keys:
		decrypted = "".join(map(chr, xor_encrypt(key, encrypted)))
		score = score_text(decrypted)
		if score > Score:
			Key, Score, Decrypted = key, score, decrypted
			_key = "".join(map(chr, key))
	problem.answer = "'{0}' {1} - {2}\n{3}".format(
		"".join(map(chr,Key)), Key, 
		sum(map(ord,Decrypted)), Decrypted)