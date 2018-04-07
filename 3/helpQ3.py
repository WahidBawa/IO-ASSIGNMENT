from random import *

###You already know how to use shuffle
nums = [1,2,3,4,5]
shuffle(nums)
print(nums)

###
###The shuffle method only works on a mutable data,so you can NOT shuffle a string.
###Thus we have to move back and forth between a string and a list. Here are some relevant methods.
###You can convert a string to a list, using the list function.
###This function adds each character of a string as an element to a list

word = "vincent"

# STRING TO LIST:
# list() function iterates through the string, 
# making each letter a string element of the list.
listOfLetters = list(word)
print(listOfLetters) ### prints ['v', 'i', 'n', 'c', 'e', 'n', 't']

# LIST TO STRING:
# join() function assembles letters of a list,
# with the lead string between each letter.
# If that lead string is the empty string, 
# it just makes the list of letters a single string.
wordString=''.join(listOfLetters)
print("That list reassembled as a string is:", wordString)
# from ['v', 'i', 'n', 'c', 'e', 'n', 't'] we can get the string "vincent"

### for the question you are solving, you need to keep the first and last letter and shuffle all other letters
###e.g. "vincent" becomes "vcninet"






