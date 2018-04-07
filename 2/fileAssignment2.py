# fileAssignment2.py
from pprint import *
from re import *
seuss = open("seuss.txt", "r").read().strip().split('\n')
dictionary = open("Dictionary.txt", "w")
words = []
for i in seuss:
	sentence = split(' |, |-',i)
	for n in sentence:
		n = n.lower().strip('.').strip('?').strip('!').strip(',').strip('[').strip(']').strip('(').strip(')').strip(';')
		if n != '':
			if n not in words:
				words.append(n)
s = "\n".join(words)
dictionary.write(s)				
# pprint(words)
pprint(len(words))