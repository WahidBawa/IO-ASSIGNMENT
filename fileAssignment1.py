#fileAssignment1.py
from pprint import *
low = int(input("ENTER THE POINTS FROM: "))
high = int(input("ENTER THE POINTS TO: "))
finalList = []
people = open("ATP.txt", "r").read().strip().split("\n")
fname = open(str(low) + "to" + str(high) + ".txt", "w")
for i in people:
	person = i.split(',')
	if int(person[-1]) >= low and int(person[-1]) <= high:
		fname.write(person[0] + ', ' + person[2] + ', ' + person[-1] + "\n")
