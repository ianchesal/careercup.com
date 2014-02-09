#!/bin/env python

'''
See: http://www.careercup.com/question?id=16759664

The Question
------------

> You have k lists of sorted integers. Find the smallest range that
> includes at least one number from each of the k lists. 
>  
> For example, 
> List 1: [4, 10, 15, 24, 26] 
> List 2: [0, 9, 12, 20] 
> List 3: [5, 18, 22, 30] 
>
> The smallest range here would be [20, 24] as it contains 24 from
> list 1, 20 from list 2, and 22 from list 3.

My Notes
--------

The min heap solution, I'll admit, wasn't obvious to me and rather
brilliant. I had originally coded this using array pointers and advancing
the pointer for the array with the smallest value on each itteration
of the loop. It worked but accounting was cubersome and I wasn't positive
it would work well for all cases. The heap solution was far more elegant
and gave me a chance to dust off my heapq knowledge in Python.

To test this code run:

    python integerranges1.py

It will execute the doctests for all code in this solution.
'''

from heapq import heappush, heappop

class RangeFinder():
	'''
	These are the test cases:

	>>> rf = RangeFinder()
	>>> rf.add_array([4, 10, 15, 24, 26])
	>>> rf.add_array([0, 9, 12, 20])
	>>> rf.add_array([5, 18, 22, 30])
	>>> print rf
	0: [4, 10, 15, 24, 26]
	1: [0, 9, 12, 20]
	2: [5, 18, 22, 30]
	array_current_index: [0, 0, 0]
	min_heap: [(0, 1), (4, 0), (5, 2)]
	>>> rf.run()
	[20, 24]
	'''
	def __init__(self):
		# A list of lists -- these are all the arrays we need to
		# look through.
		self.arrays = list()
		# Pointers to the current index in the arrays we're considering
		self.array_current_index = list()
		self.min_heap = []

	def __str__(self):
		'''
		Print a string representation of the class that's useful
		for debugging.
		'''
		retval = ''
		for i in range(0,len(self.arrays)):
			retval = retval + '%s: %s\n' % (i, self.arrays[i])
		retval = retval + 'array_current_index: %s\n' % self.array_current_index
		retval = retval + 'min_heap: %s' % self.min_heap
		return retval

	def add_array(self, array):
		'''
		Add a new array to the class.
		'''
		if len(array) < 1:
			raise Error('Array size 0 not supported')
		self.arrays.append(array)
		self.array_current_index.append(0)
		array_index = len(self.arrays) - 1
		# On the head we track the minimum value from the array and the
		# index of the array the minimum value came from as a tuple:
		#   (value, array index value came from)
		heappush(self.min_heap, (self.arrays[array_index][0], array_index))

	def run(self):
		'''
		Run the algorithm that finds the smallest range that contains
		values from all the arrays added to the class. Return an array
		representing the range.
		'''
		range_pair = list()
		stop = False
		while not stop:
			current_minimum = heappop(self.min_heap)
			current_minimum_value = current_minimum[0]
			minimum_array = current_minimum[1]
			minimum_array_index = self.array_current_index[minimum_array]
			if minimum_array_index + 1 < len(self.arrays[current_minimum[1]]):
				# If there's still stuff left in this array keep going.
				# Put the next value from this array on the heap and run
				# through the loop again.
				heappush(self.min_heap, (self.arrays[minimum_array][minimum_array_index + 1], minimum_array))
				# Move the pointer for this array ahead by one in our tracking
				# data structure.
				self.array_current_index[minimum_array] = minimum_array_index + 1
			else:
				# If there's nothing left on this array we're done. We've
				# found the smallest range. That contains elements from all
				# the arrays we were given. Construct it and return.
				stop = True
				maximum = self.min_heap[-1][0]
				range_pair.append(current_minimum_value)
				range_pair.append(maximum)
		# Reset everything so we can run it again and again on the same
		# data and get the same result.
		self.min_heap = []
		for i in range(0,len(self.arrays)):
			self.array_current_index[i] = 0
			heappush(self.min_heap, (self.arrays[i][0], i))
		return range_pair

if __name__ == '__main__':
	import doctest
	doctest.testmod()