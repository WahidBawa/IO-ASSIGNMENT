# fileAssignment3.py
from random import * ; from pprint import * # imports random and pretty print
words = open("testing.txt", "r").read().strip().split('\n') # opens the file that I want to read from to mix up the letters
fname = open("MixedFile.txt", "w") # This opens / creates a file that will store the text after it is mixed up
l = [] ; mixedList = [] # creates initial list and the list that will store the mixed sentence
for i in words:# starts the loop that will add the words to a list so that they are ready to be mixed up
	word = i.split(" ") # sepperates the words wherever there is a space
	for n in word: # will append the individual words to the initial list
		l.append(n)
for i in l:# this is the loop that will run the process of mixing up the words
	mx = list(i)# creates a list out of the string
	if len(mx) > 3:# This is will only mix up the words if they are longer than 3 letters in length
		l1, l2 = mx[0], mx[-1] ; del mx[0] ; del mx[-1] # this will assign the first and last letters 
														# to a variable and will delete them from the list
		shuffle(mx) # this will mixup the remaining letters
		mx.insert(0, l1) ; mx.append(l2) # this will insert the first and last letters back into their correct spots
	mixString = ''.join(mx) + ' ' # this will condense the contents of the mixed up list into a string
	mixedList.append(mixString) # this will then append to the list that stores the mixed up words
s = ''.join(mixedList) # this will condense the list that contains the mixed up words in to a single string
fname.write(s) # this writes the mixed up sentences / paragraphs to a text file