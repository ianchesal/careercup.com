#!/bin/env python

'''
This was from an interview I did.

The Question
------------

> Given a set of characters, produce all permutations of subsets from
> the characters in the set including the empty set and the set itself.
>
> Examples:
>
> 	ab   -> ('', a , b, ab)
>   abc  -> ('', a, b, c, ab, ac, bc, abc)
>   abcd -> ('', a, b, c, d, ab, ac, ad, bc, bd, cd, abc, abd, acd, bcd, abcd)

My Notes
--------

I'll say this: I didn't get the right solution in the interview. I got
a working answer fairly fast doing some pointer-type code with indices
and windows/slices on the iterables, but it missed some permutations.

As time ran down I was getting closer to the solution but didn't have
time to code it. This bugged me. I completed the code on the way home
and wanted to write it down.

They key to my downfall on this question was I hadn't reviewed O(2^N)
algorithm patterns. Quite honestly: it's been nearly 20 years since I've
had an exposure to an algorithm with that complexity and when I did it
was in university. Algorithms with this complexity just don't show up in
my working life where I'm largely consumed by DAG algorithms and array
algorithms.

I certainly won't forget O(2^N) algorithms now!

I did manage to spot that the complexity was O(2^N) by writing out
some solutions to an increasing number of longer sets:

    Set Size     Output Size
     1            2
     2            4
     3            8
     4            16

I just couldn't connect that with at design pattern for an alogithm in
time.

In any case: I give you the proper solution. An O(2^N) algorithm that
produces the correct output.
'''

def permutations(iterable):
	'''
	For an iterable set, return all the permutations of things in the
	set as a list. Inclues the empty set and the set itself.

	>>> permutations('')
	['']
	>>> len(permutations(''))
	1
	>>> permutations('a')
	['', 'a']
	>>> len(permutations('a'))
	2
	>>> permutations('ab')
	['', 'a', 'b', 'ab']
	>>> len(permutations('ab'))
	4
	>>> permutations('abc')
	['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
	>>> len(permutations('abc'))
	8
	>>> permutations('abcd')
	['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc', 'd', 'ad', 'bd', 'abd', 'cd', 'acd', 'bcd', 'abcd']
	>>> len(permutations('abcd'))
	16
	>>> len(permutations('abcde'))
	32
	>>> len(permutations('abcdef'))
	64
	'''
	# Start with the empty case:
	collector = ['']
	# For each thing in iterable, permute thing with collector and
	# then add the result to the existing collector value.
	for character in iterable:
		collector = collector + _permutations_helper(collector, character)
	return collector

def _permutations_helper(iterable, character):
	'''
	For each thing in iterable, appends character to that thing and
	stores it in an array. Returns the list of character appended to
	each thing in iterable.

	>>> _permutations_helper((''), 'a')
	['a']
	>>> _permutations_helper(('', 'a'), 'b')
	['b', 'ab']
	>>> _permutations_helper(('', 'a', 'b'), 'c')
	['c', 'ac', 'bc']
	'''
	return_array = list()
	if len(iterable) == 0:
		# The empty case has to be handled properly.
		return_array.append(character)
	else:
		for item in iterable:
			return_array.append(item + character)
	return return_array

if __name__ == '__main__':
	import doctest
	doctest.testmod()
