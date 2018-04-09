#fileAssignment1.py
from pprint import * # imports pretty print
people = open("ATP.txt", "r").read().strip().split("\n") # this will open the file that stores the information on the people
low, high = int(input("ENTER THE POINTS FROM: ")), int(input("ENTER THE POINTS TO: ")) # allows the user to enter in the values
fname = open(str(low) + "to" + str(high) + ".txt", "w") # will create the txt file that will store the participants
for i in people: # this will go through the participants and will split them into individual values
	person = i.split(',')
	if int(person[-1]) >= low and int(person[-1]) <= high: # if the persons points are more than low and less than high
		fname.write(person[0] + ', ' + person[2] + ', ' + person[-1] + "\n") # this will write the information 
																			 # of the participant to the list