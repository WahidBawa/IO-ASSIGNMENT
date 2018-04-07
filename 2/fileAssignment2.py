# fileAssignment2.py
from pprint import *
seuss = open("seuss.txt", "r").read().strip().split('\n')
words = []
for i in seuss:
	sentence = i.split(' ')
	for n in sentence:
		n = n.lower().strip('.').strip('?').strip('!').strip(',')#.strip('[').strip(']').strip('(').strip(')').strip(';')
		if n != '':
			if n not in words:
				words.append(n)
pprint(words)
pprint(len(words))