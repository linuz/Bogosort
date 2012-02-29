#!/usr/bin/python
#############################################################
# Bogosort for Python										#
# by: Dennis Linuz <dennismald@gmail.com>					#
# Demonstration of a bogosort.								#
#############################################################

import random,time,sys

#Input your list of numbers as arguments
input_array=[]
if (len(sys.argv) < 2):
	print ""
	print "Please input list items as arguments"
	print "\nExample: ./bogosort.py <item1> [item2] [item3] [item4] ..."
	quit()
i=1
while (i < len(sys.argv)):
	input_array.append(int(sys.argv[i]))
	i+=1

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
	while (i < len(array)-1):
		if not (array[i] <= array[i+1]):
			return False
		i+=1
	return True

testArray=input_array
count = 0
time1 = time.time()
while (not isOrdered(testArray)):
	print "Shuffling: " + str(testArray)
	testArray = randomizeList(testArray)
	count += 1
print ""
print "Sorted after " + str(count) + " tries."
print "Sorted:  " + str(testArray)
print "---"
print "Overall Time: " + str(time.time()-time1) + " seconds"
