#!/bin/env python

'''
This was from an interview I did.

The Question
------------

> Implement a memcached class. Where the class takes a key/value pair
> for addition and can return a key for a value. It should have a limit
> on the key/value pairs it can store in the cache and an LRU algorithm
> for purging old values when the cache gets full.


Tests and Examples
------------------

>>> c = Cache(max_size=3)
>>> c.put(1, 'one')
>>> c.put(2, 'two')
>>> c.put(3, 'three')
>>> c.get(1)
'one'

When we got 1 we caused it to be the MRU object in the cache. So adding
something new should cause 2 to be purged:

>>> c.put(4, 'four')
>>> print c.have.keys()
[1, 3, 4]
>>> c.get(2)


Adding a value at key 2 back in should now cause 3 to get purged because
it's the LRU object in the cache now.

>>> c.put(2, 'two')
>>> print c.have.keys()
[1, 2, 4]
>>> c.get(2)
'two'
>>> c.get(3)

Updating the value stored for key 4 should work:

>>> c.put(4, 'five')
>>> c.get(4)
'five'


My Notes
--------

My initial solution to this in the interview was good, but not the best,
approach to solving the problem. I had O(1) get() and O(1) put() when
there was space in the cache. But I had an O(N) solution for put() when
the cache was full and I needed to purge the LRU item from the cache.

I was able to sort out an all-around O(1) solution to put() after thinking
about it some more.

The key was to use both a hash and a linked list to track the data. The
hash for O(1) look ups for hits and for accessing the data and the linked
list to keep a queue sorted by access order so it's easy to get at the
LRU item in constant time.

Some problems just won't leave your head until you've licked them.
'''

import time

class CacheValue():
	'''
	Holds values in the cache along with the key and the last time
	the value was accessed. Technically the time isn't required but
	a future enhancement to this implementation might be support
	for a side process that does stale cached item purging and having
	the time stamps would help with that algorithm.
	'''

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.time = time.time()
		# For the double linked list data structure
		self.older = None
		self.newer = None

	def touch(self):
		self.time = time.time()

class Cache():

	def __init__(self, max_size):
		self.max_size = max_size
		self.have = dict()
		self.oldest = None # Pointer to the tail of the linked list
		self.newest = None # Pointer to the head of the linked list

	def put(self, key, value):
		'''
		Put a new value in to the cache. If we're out of space, purge
		the LRU object in to the cache to make room. If the key exists
		already update the value stored at that key.
		'''
		if key in self.have:
			self.have[key].value = value
		else:
			if len(self.have.keys()) == self.max_size:
				# Purge the LRU object
				temp = self.oldest
				self.oldest = temp.newer
				self.oldest.older = None
				del(self.have[temp.key])
				del(temp)
			temp = CacheValue(key, value)
			if self.newest:
				temp.older = self.newest
				self.newest.newer = temp
			if not self.oldest:
				self.oldest = temp
			self.newest = temp
			self.have[temp.key] = temp

	def get(self, key):
		'''
		Check the cache for a key. If it exists return the value, otherwise
		return None.

		>>> c = Cache(max_size=1)
		>>> c.put(1, 'one')
		>>> c.get(1)
		'one'
		>>> c.get(2)
		>>> c.get(3)
		'''
		if key not in self.have:
			return None
		# Need to put this accessed key on the head of our linked list
		# because it's now the MRU cached item.
		temp = self.have[key]
		temp.touch()
		# We don't need to do this if it's already the MRU object. The
		# MRU object has newer pointing to None.
		if temp.newer:
			# Remove temp from the doubly linked list. Redirecting anything
			# it's pointing to on either side to each other.
			temp.newer.older = temp.older
			self.oldest = temp.newer
			if temp.older:
				temp.older.newer = temp.newer
			self.newest.newer = temp
			temp.older = self.newest
			temp.newest = None
			self.newest = temp
		return self.have[key].value

if __name__ == '__main__':
	import doctest
	doctest.testmod()
