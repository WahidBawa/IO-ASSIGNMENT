# fileAssignment3.py
from random import * ; from pprint import *
words = open("testing.txt", "r").read().strip().split('\n')
fname = open("MixedFile.txt", "w")
l = [] ; mixedList = []
for i in words:
	word = i.split(" ")
	for n in word:
		l.append(n)
for i in l:
	mx = list(i)
	if len(mx) > 3:
		l1, l2 = mx[0], mx[-1] ; del mx[0] ; del mx[-1]
		shuffle(mx)
		mx.insert(0, l1) ; mx.append(l2)
	mixString = ''.join(mx) + ' '
	mixedList.append(mixString)
s = ''.join(mixedList)
fname.write(s)