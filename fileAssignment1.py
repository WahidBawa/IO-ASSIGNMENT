#fileAssignment1.py
from pprint import *
people = open("ATP.txt", "r").read().strip().split("\n")
low, high = int(input("ENTER THE POINTS FROM: ")), int(input("ENTER THE POINTS TO: "))
fname = open(str(low) + "to" + str(high) + ".txt", "w")
for i in people:
	person = i.split(',')
	if int(person[-1]) >= low and int(person[-1]) <= high:
		fname.write(person[0] + ', ' + person[2] + ', ' + person[-1] + "\n")