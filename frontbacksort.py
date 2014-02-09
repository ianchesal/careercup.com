#!/bin/env python

'''
See: http://www.careercup.com/question?id=5201559730257920

To test this code run:

    python frontbacksort.py

It will execute the doctests for all code in this solution.
'''

class Node:
	'''
	A node in a linked list.

	>>> n = Node(1000, None)
	>>> print n
	[1000]
	'''
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return '[' + str(self.value) + ']'

class LinkedList:
	'''
	A linked list formed out of Node objects.
	'''

	def __init__(self, values=None):
		'''
		Create a new LinkedList object. Bootstrap it from an
		array of values if you want.

		>>> ll = LinkedList()
		>>> ll.length
		0
		>>> ll.append(1)
		>>> ll.length
		1
		>>> ll.last.value
		1
		>>> otherll = LinkedList([1, 2, 3])
		>>> otherll.length
		3
		>>> otherll.first.value
		1
		>>> otherll.last.value
		3
		'''
		self.first = None
		self.last = None
		self.length = 0
		if values:
			for i in values:
				self.append(i)

	def __str__(self):
		'''
		Print a string representation of the list.

		>>> ll = LinkedList([1, 2, 3])
		>>> print ll.length
		3
		>>> print ll
		[1] -> [2] -> [3]
		'''
		current = self.first
		rep = ''
		while current:
			if rep:
				rep = rep + ' -> ' + str(current)
			else:
				rep = str(current)
			current = current.next
		return rep

	def clear(self):
		'''
		Wipe the linked list, set it back to no elements.

		>>> ll = LinkedList([1, 2, 3])
		>>> ll.length
		3
		>>> ll.clear()
		>>> ll.length
		0
		'''
		self.first = None
		self.last = None
		self.length = 0

	def append(self, value):
		'''
		Append a new value to a linked list.

		>>> ll = LinkedList()
		>>> ll.append(1)
		>>> print ll.length
		1
		>>> ll.append(1)
		>>> print ll.length
		2
		>>> print ll.last.value
		1
		'''
		if not self.first:
			self.first = Node(value, None)
			self.last = self.first
		elif self.first == self.last:
			self.last = Node(value, None)
			self.first.next = self.last
		else:
			new = Node(value, None)
			self.last.next = new
			self.last = new
		self.length = self.length + 1

	def array(self):
		'''
		Return an array of values from all the nodes in the
		list.

		>>> ll = LinkedList([1, 2, 3])
		>>> ll.length
		3
		>>> ll.array()
		[1, 2, 3]
		'''
		a = list()
		current = self.first
		while current:
			a.append(current.value)
			current = current.next
		return a

def _move_forward(array, i):
	'''
	Move the value at position i in the array forward, swapping
	with values ahead of it as you go, until the value ahead of
	it is a positive integer value. Return True if you had to
	move something, false if you didn't have to move something.

	The array is changed in place.

	>>> a = [1, -2, 3]
	>>> _move_forward(a, 0)
	True
	>>> print a
	[-2, 1, 3]
	>>> a = [1, 2, -3]
	>>> _move_forward(a, 0)
	False
	>>> print a
	[1, 2, -3]
	>>> a = [1, 2, -3]
	>>> _move_forward(a, -1)
	False
	>>> print a
	[1, 2, -3]
	>>> a = [1, 2, -3]
	>>> _move_forward(a, 3)
	False
	>>> print a
	[1, 2, -3]
	>>> a = [1, -2, -3]
	>>> _move_forward(a, 0)
	True
	>>> print a
	[-2, -3, 1]
	>>> a = [1, 2, 3]
	>>> _move_forward(a, 2)
	False
	>>> print a
	[1, 2, 3]
	>>> a = [1, 2]
	>>> _move_forward(a, 3)
	False
	>>> print a
	[1, 2]
	>>> a = [1, 2, 3]
	>>> _move_forward(a, 2)
	False
	>>> print a
	[1, 2, 3]
	'''
	done_moves = False
	made_moves = False
	if i < 0 or i >= len(array):
		# Bad input. We're done.
		done_moves = True
	while i < len(array)-1 and not done_moves:
		if array[i+1] < 0:
			# Move it forward one more spot
			t = array[i]
			array[i] = array[i+1]
			array[i+1] = t
			i = i + 1
			made_moves = True
		else:
			# We're done. The next number is positive so we
			# need to stop moving this value foward.
			done_moves = True
	return made_moves

def _move_backward(array, i):
	'''
	Move the value at position 1 in teh array backward, swapping
	with values behind it as you go, until the value behind it is
	a negative integer value. Return True if you had to
	move something, false if you didn't have to move something.

	The array is changed in place.

	>>> a = [1, -2, 3]
	>>> _move_backward(a, 0)
	False
	>>> print a
	[1, -2, 3]
	>>> a = [1, -2, 3]
	>>> _move_backward(a, -1)
	False
	>>> print a
	[1, -2, 3]
	>>> a = [1, -2, 3]
	>>> _move_backward(a, 3)
	False
	>>> print a
	[1, -2, 3]
	>>> a = [1, -2, 3]
	>>> _move_backward(a, 1)
	True
	>>> print a
	[-2, 1, 3]
	>>> a = [1, -2, 3]
	>>> _move_backward(a, 2)
	False
	>>> print a
	[1, -2, 3]
	>>> a = [-1, -2, 3]
	>>> _move_backward(a, 1)
	False
	>>> print a
	[-1, -2, 3]
	>>> a = [-1, 2, 3]
	>>> _move_backward(a, 2)
	True
	>>> print a
	[-1, 3, 2]
	>>> a = [1, 2, -3]
	>>> _move_backward(a, 2)
	True
	>>> print a
	[-3, 1, 2]
	'''
	done_moves = False
	made_moves = False
	if i < 0 or i >= len(array):
		# Bad input. We're done.
		done_moves = True
	while i > 0 and not done_moves:
		if array[i-1] >= 0:
			# Move it backward one more spot
			t = array[i]
			array[i] = array[i-1]
			array[i-1] = t
			i = i - 1
			made_moves = True
		else:
			# We're done. The next number to the left of this one is
			# negative so we need to stop moving this value backward.
			done_moves = True
	return made_moves

def frontback_linkedlist(array):
	'''
	Sort an array of integers such that all the negative integers
	appear in the first half of the array and the positive integers
	appear in the second half of the array. Maintain the *order* of
	the integers though, that shouldn't be changed.

	The function treats 0 like it's a positive integer.

	It uses a linked list approach which gives you O(N) operation but
	because we have to build the linked list out of the array it's
	also Size(N) -- which doesn't gain you anything over the much,
	much simpler frontback_array() approach.

	I did this mainly for academic interest to play around with
	linked lists in Python.

	>>> frontback_linkedlist([-1, 2])
	[-1, 2]
	>>> frontback_linkedlist([1, -2])
	[-2, 1]
	>>> frontback_linkedlist([-1, 1, 3, -2, 2])
	[-1, -2, 1, 3, 2]
	>>> frontback_linkedlist([1, 2, -3, -4])
	[-3, -4, 1, 2]
	>>> frontback_linkedlist([-1, 2, -3, 4, -5])
	[-1, -3, -5, 2, 4]
	>>> frontback_linkedlist([1, -2, 3, -4, 5, -6, 7])
	[-2, -4, -6, 1, 3, 5, 7]
	'''
	linkedlist = LinkedList(array)

	# Find the first node in the list where the next node is a positive
	# number. This is where we'll start inserting negative numbers we
	# find elsewhere in the list.
	last_negative_number = None
	node = linkedlist.first
	while node.value < 0 and node.next and node.next.value < 0:
		node = node.next
	if node.value < 0:
		last_negative_number = node

	# Now start removing negative values from the list and moving
	# them back to the last negative value position. Moving the last
	# negative value position ahead by one every time we do this.
	while node.next:
		if node.next.value < 0:
			# Pop this node out of the list
			popped_node = node.next
			node.next = popped_node.next
			# And insert it in to the list at the spot where we
			# saw the last negative value.
			if last_negative_number:
				popped_node.next = last_negative_number.next
				last_negative_number.next = popped_node
			else:
				popped_node.next = linkedlist.first
				linkedlist.first = popped_node
			# Now move the last negative value pointer ahead to
			# this newly inserted node.
			last_negative_number = popped_node
		else:
			node = node.next
	return linkedlist.array()

def frontback_array(array):
	'''
	Sort an array of integers such that all the negative integers
	appear in the first half of the array and the positive integers
	appear in the second half of the array. Maintain the *order* of
	the integers though, that shouldn't be changed.

	The function treats 0 like it's a positive integer.

	This uses a two array approach: storing negative values encountered
	in one array, positive values in another, and then returning the
	concatenation of the two arrays. It's O(N) in operation but Size(N)
	because it's essentially storing twice the data.

	>>> frontback_linkedlist([-1, 2])
	[-1, 2]
	>>> frontback_linkedlist([1, -2])
	[-2, 1]
	>>> frontback_linkedlist([-1, 1, 3, -2, 2])
	[-1, -2, 1, 3, 2]
	>>> frontback_linkedlist([1, 2, -3, -4])
	[-3, -4, 1, 2]
	>>> frontback_linkedlist([-1, 2, -3, 4, -5])
	[-1, -3, -5, 2, 4]
	>>> frontback_linkedlist([1, -2, 3, -4, 5, -6, 7])
	[-2, -4, -6, 1, 3, 5, 7]
	'''
	negatives = list()
	positives = list()
	for i in array:
		if i < 0:
			negatives.append(i)
		else:
			positives.append(i)
	return negatives + positives

def frontback_moving(array):
	'''
	Sort an array of integers such that all the negative integers
	appear in the first half of the array and the positive integers
	appear in the second half of the array. Maintain the *order* of
	the integers though, that shouldn't be changed.

	The function treats 0 like it's a positive integer.

	This uses in-place moves on the array to shuffle data around and
	sort it. The operation time is awful at O(N^2) but the implemention
	is Size(1), using only one extra integer value to move the array
	data.

	>>> frontback_linkedlist([-1, 2])
	[-1, 2]
	>>> frontback_linkedlist([1, -2])
	[-2, 1]
	>>> frontback_linkedlist([-1, 1, 3, -2, 2])
	[-1, -2, 1, 3, 2]
	>>> frontback_linkedlist([1, 2, -3, -4])
	[-3, -4, 1, 2]
	>>> frontback_linkedlist([-1, 2, -3, 4, -5])
	[-1, -3, -5, 2, 4]
	>>> frontback_linkedlist([1, -2, 3, -4, 5, -6, 7])
	[-2, -4, -6, 1, 3, 5, 7]
	'''
	i = 0
	while i < len(array):
		if array[i] < 0:
			moved = _move_backward(array, i)
		else:
			moved = _move_forward(array, i)
		if not moved:
			i = i + 1
	return array

if __name__ == '__main__':
	import doctest
	doctest.testmod()
