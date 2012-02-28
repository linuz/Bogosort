#!/usr/bin/python
#############################################################
# Bogo-Sort for Python										#
# by: Dennis Linuz <dennismald@gmail.com>					#
# Demonstration of a bogo-sort								#
#############################################################
def randomizeList(array):
	
	
def isOrdered(array):
	i = 0
	while (i < len(array)):
		print "Looped"
		if i < len(array)-1:
			if not (array[i] < array[i+1]):
				return False
		i+=1
	return True


testArray = ([1,22,3,4])
print isOrdered(testArray)
