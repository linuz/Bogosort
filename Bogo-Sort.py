#!/usr/bin/python
#############################################################
# Bogo-Sort for Python										#
# by: Dennis Linuz <dennismald@gmail.com>					#
# Demonstration of a bogo-sort								#
#############################################################

#Input your list of numbers here!
INPUT_ARRAY = ([1,2,5,3,6,8])

import random
#Shuffle the array items into a random order
def randomizeList(array):
	for x in xrange(0,len(array)):
		randomNumber = int(random.random()*len(array)-1)	
		if (not(x == randomNumber)):
			tempVar = array[x]
			array[x] = array[randomNumber]
			array[randomNumber] = tempVar
	return array
	
#Check if the array is in order from least to greated
def isOrdered(array):
	i = 0
	while (i < len(array)):
		if (i < len(array)-1):
			if not (array[i] <= array[i+1]):
				return False
		i+=1
	return True


testArray=INPUT_ARRAY
count = 0
while (not isOrdered(testArray)):
	print "Shuffling: " + str(testArray)
	testArray = randomizeList(testArray)
	count += 1
print ""
print "Sorted after " + str(count) + " tries."
print "Sorted: " + str(testArray)
