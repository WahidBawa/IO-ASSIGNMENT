# fileAssignment2.py
from pprint import * ; from re import * # imports the pretty print and allows me to split multiple times by importing re
seuss = open("hamlet.txt", "r").read().strip().split('\n') # opens the file that I will read the information / story from
dictionary = open("Dictionary.txt", "w") # Opens / creates a file that will store the unique words used in the story
w = set() # stores the unique words in the story
p = list("!#$%&()*+,-./:;<=>?@[\]^_`{|}~") # stores the punctuation
for i in seuss: # will go through the sentences in the story and will split it on spaces, commas, and dashes / minus signs
	sentence = split(' |, |-',i)
	for n in sentence:# will go through the words and will make them lower cas and will remove it of punctuation
		n = n.lower()
		for letter in n:
			if letter in p:
				n = n.replace(letter, "")
		if n != '': # if n is not empty and n is not already added to the w set, then n will be added to the words list
			w.add(n)
s = "\n".join(w)# this will condense the unique words into strings
dictionary.write(s) # this will write the unique words to the Dictionary.txt file
pprint(w) # This can be uncommented to see the unique words (USE AT RISK OF CRASHING COMPUTER)
print(len(w)) # this will print the amount of unique words used in the story