#!/bin/env python

'''
See: http://www.careercup.com/question?id=6287528252407808

The Question
------------

> A k-palindrome is a string which transforms into a palindrome on
> removing at most k characters. 
> 
> Given a string S, and an interger K, print "YES" if S is a k-palindrome;
> otherwise print "NO". 
> 
> Constraints: 
> S has at most 20,000 characters. 
> 0<=k<=30 
> 
> Sample Test Case#1: 
> Input - abxa 1 
> Output - YES 
> Sample Test Case#2: 
> Input - abdxa 1 
> Output - No

My Notes
--------

I went at this one after having refreshed my knowledge of Python's
itertools package. I thought I could make good use of
itertools.combinations to work up a solution to this problem.

The solution is short and elegant with the use of this module but
I fear the time complexity isn't that great. It's bounded by the
complexity of itertools.combinations since I'll be running that
function, at worst, k times to get the combinations of the string
with items removed. The naive implementation of combinations is
O(N^2) so this is O( k * N^2 ) which reduces to O(N^2). Hopefully
the itertools.combinations() implementaiton isn't naive.

To test this code run:

    python kpalindromes.py

It will execute the doctests for all code in this solution.
'''

from itertools import combinations

class KPalindromeFinder():
	'''
	Finds k-palindromes in a string for a given value of k.

	>>> kp = KPalindromeFinder('abxa', 1)
	>>> kp.run()
	True
	>>> kp = KPalindromeFinder('abdxa', 1)
	>>> kp.run()
	False
	>>> kp = KPalindromeFinder('abdxa', 2)
	>>> kp.run()
	True
	'''
	def __init__(self, string, k):
		self.string = string
		self.k = k

	def run(self):
		'''
		Do the actual search. Returns a list of the largest
		k-palindrome sub-words found in the string.
		'''
		# We'll start by looking at the string, then the string
		# minus one character, then minus two characters and so
		# on all the way up to k characters.
		#
		# Every time we generate a combination of sub-strings we'll
		# test those to see if any of them are palindromes and stop
		# as soon as we find one case where this is the case.
		i = len(self.string)
		while i >= len(self.string) - self.k:
			for word in combinations(self.string, i):
				if self._is_palindrome(word):
					return True
			i = i - 1
		return False

	def _is_palindrome(self, word):
		'''
		Returns true if word is a palidrome, otherwise False.

		>>> kp = KPalindromeFinder(None, None)
		>>> kp._is_palindrome('a')
		True
		>>> kp._is_palindrome('ab')
		False
		>>> kp._is_palindrome('aba')
		True
		>>> kp._is_palindrome('abba')
		True
		>>> kp._is_palindrome('abc')
		False
		'''
		if word == word[::-1]:
			return True
		return False

if __name__ == '__main__':
	import doctest
	doctest.testmod()