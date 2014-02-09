#!/bin/env python

'''
See: http://www.careercup.com/question?id=24532662

The Question
------------

> You are given two array, first array contain integer which represent heights of
> persons and second array contain how many persons in front of him are standing
> who are greater than him in term of height and forming a queue. Ex 
> A: 3 2 1 
> B: 0 1 1 
>
> It means in front of person of height 3 there is no person standing, person
> of height 2 there is one person in front of him who has greater height then
> he, similar to person of height 1. Your task to arrange them 
>
> Ouput should be. 
> 
> 3 1 2 
> 
> Here - 3 is at front, 1 has 3 in front ,2 has 1 and 3 in front.

My Notes
--------

Reading over the answers I was little perplexed as to why people weren't
using trees to store the data. My first thought was a binary tree with
some special accounting to guide left vs. right insertion decisions could
help form the line quickly.

The solution I wrote assumes the input isn't ever wrong. That is: you're
always given data that has a solution to it, that isn't impossible to solve.
It also tries to solve for the most perfect case. That is, if Person A wants
3 higher people in front of them it tries to give them exactly three higher
people in front of them, not 3 or fewer higher people in front of them.

As you can see: the tree approach works, and it works really well here.

We know the end state we desire for each node, we know how to do the
accounting to track who is ahead of the node and higher than them, so 
we can make tree insertion decisions by looking at just data on each
node as we move through the tree to try and figure out where to put a
new node.

This makes the average run time O(log N) (standard binary tree) with a
worst-case insertion of O(N).

To test this code run:

    python lineofpeople.py

It will execute the doctests for all code in this solution.
'''

class Person():
	'''
	The Person class is a node in a tree of people. It has the property
	that there are no more than N people higher than this person
	stored in the right hand branch of the sub-tree off this node.

	For example: if higher_than was 0 the rightbranch will be None. If
	higher_than is 1 the rightbranch will point to one node, that node 
	will have no left or right children.

	>>> p = Person(1, 0)
	>>> isinstance(p, Person)
	True
	>>> print p
	[1, 0, 0]
	>>> p.insert(Person(1,0))
	>>> print p
	[1, 0, 0]
	[1, 0, 0]
	>>> p.insert(Person(0,1))
	>>> print p
	[1, 0, 0]
	[0, 1, 1]
	[1, 0, 0]
	'''
	def __init__(self, height, higher_than):
		self.height = height
		self.higher_than = higher_than
		self.higher_ahead_of_us = 0
		self.equal_ahead_of_us = 0
		# We'll name our two branches behind and ahead instead of left
		# and right so reading the code makes it a little more obvious
		# what we're doing when we insert another person at this person's
		# location.
		self.behind = None
		self.ahead = None

	def __str__(self):
		'''
		Print everyone ahead of me, then me, then everyone
		behind me.
		'''
		retval = ''
		if self.ahead:
			retval = retval + str(self.ahead)
		if retval != '':
			retval = retval + '\n'
		retval = retval + '[%s, %s, %s]' % (self.height, self.higher_than, self.higher_ahead_of_us)
		if self.behind:
			retval = retval + '\n' + str(self.behind)
		return retval

	def insert(self, person):
		'''
		Inserts a new person so that this person doesn't violate the
		rules.
		'''
		if person > self:
			# This person is higher than us. See if they can go
			# to the left or right of us.
			if self.higher_than - self.higher_ahead_of_us > 0:
				# We want people higher than us ahead of us and there's
				# still room ahead of us for higher people. This person
				# could possibly go ahead of us.
				if self.ahead:
					self.ahead.insert(person)
				else:
					self.ahead = person
				self.higher_ahead_of_us = self.higher_ahead_of_us + 1
			else:
				# We have no room for people higher than us to go
				# in front of us. Put this person behind us.
				if self.behind:
					self.behind.insert(person)
				else:
					self.behind = person
		elif person == self:
			# This person is the same height as us. They can go behind
			# us if they ultimately want as many or more higher people in
			# front of them than we do. Otherwise they have to go ahead
			# of us.
			if person.higher_than >= self.higher_than:
				if self.behind:
					self.behind.insert(person)
				else:
					self.behind = person
				# Note that this person now has one more person the
				# same height as them ahead of them.
				person.equal_ahead_of_us = person.equal_ahead_of_us + 1
			else:
				if self.ahead:
					self.ahead.insert(person)
				else:
					self.ahead = person
				# Count people our height ahead of us so we can make
				# better decisions for future insertions in to the line.
				self.equal_ahead_of_us = self.equal_ahead_of_us + 1
		else:
			# This person is shorter than us. They can go behind us
			# if they can have higher people in front of them, otherwise
			# they should go ahead of us.
			if person.higher_than > 0:
				# They need higher people in front of them. But they
				# must require 1 + self.higher_people + self.equal_ahead_of_us
				# in front of them otherwise they'll end up with more or 
			    # fewer higher people in front of them than they want.
				if person.higher_than == self.higher_than + self.equal_ahead_of_us + 1:
					# Put this person behind us and note that they have
					# self.higher_than + self.equal_ahead_of_us + 1 higher
					# people in front of them already. This may not be true
					# right now but the end state should require this to be
					# true and marking this now will help make correct
					# insertion decisions later.
					person.higher_ahead_of_us = self.higher_than + self.equal_ahead_of_us + 1
					if self.behind:
						self.behind.insert(person)
					else:
						self.behind = person
				else:
					# Put this person ahead of us. This person is shorter
					# than us so we don't have to do an accounting for them
					# on our object, just put them in the line ahead of us.
					if self.ahead:
						self.ahead.insert(person)
					else:
						self.ahead = person
			else:
				# This person can't have higher people in front of them.
				# They have to go ahead of us. No accounting on our object
				# required for them.
				if self.ahead:
					self.ahead.insert(person)
				else:
					self.ahead = person

	def __cmp__(self, b):
		'''
		Comparison operation for the Person node class. Let's you <,
		<=, >, >=, ne, eq type operations on this class.

		>>> pa = Person(1,0)
		>>> pb = Person(1,0)
		>>> pc = Person(0,0)
		>>> pd = Person(2,0)
		>>> pa == pb
		True
		>>> pa < pb
		False
		>>> pa > pb
		False
		>>> pa != pb
		False
		>>> pa == pc
		False
		>>> pa < pc
		False
		>>> pa > pc
		True
		>>> pa != pc
		True
		>>> pa == pd
		False
		>>> pa < pd
		True
		>>> pa > pd
		False
		>>> pa != pd
		True
		'''
		if isinstance(b, Person):
			if self.height < b.height:
				return -1
			elif self.height > b.height:
				return 1
			else:
				return 0
		else:
			return NotImplemented

class LineOfPeople():
	'''
	Create a line of people by arranging them based on height and based
	on their tolerance for having higher people come after them in the
	line.

	This is the test case from the original question on careercup.com:

	>>> line = LineOfPeople([3, 2, 1], [0, 1, 1])
	>>> print line
	3 1 2

	And these are some additional test cases:
	
	>>> line = LineOfPeople([1, 1, 0], [0, 0, 1])
	>>> print line
	1 0 1
	'''
	def __init__(self, heights, higher_thans):
		self.head = None
		for pairs in zip(heights, higher_thans):
			p = Person(pairs[0], pairs[1])
			self.insert(p)

	def insert(self, person):
		'''
		Adds a new person to the line. Inserting the person in to a spot
		in the line based on their height and their tolerance for having
		people higher than them in front of them in the line.
		'''
		if not self.head:
			self.head = person
		else:
			self.head.insert(person)

	def __str__(self):
		return self.__print_line_from_node(self.head)

	def __print_line_from_node(self, node):
		'''
		Used to help walk the tree and print it out in the
		format demanded by the question. I went with a separate
		printer for the LineOfPeople class because it let me keep
		the more debug-friendly Person.__str__() method and get
		the best of both worlds.
		'''
		retval = ''
		if node:
			if node.ahead:
				retval = retval + self.__print_line_from_node(node.ahead)
			if retval != '':
				retval = retval + ' '
			retval = retval + '%s' % node.height
			if node.behind:
				retval = retval + ' ' + self.__print_line_from_node(node.behind)
		if retval == '':
			retval = '<EMPTY TREE>'
		return retval

if __name__ == '__main__':
	import doctest
	doctest.testmod()