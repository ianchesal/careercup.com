'''
quicksort

Sorts an array using the quicksort approach to sorting. For example:

>>> quicksort([2,1])
[1, 2]
>>> quicksort([4,5,3,1])
[1, 3, 4, 5]

'''

def quicksort(array):
	'''
	Sorts an array using the quicksort algorithm. Returns the sorted
	array.

	>>> quicksort([])
	[]
	>>> quicksort([1])
	[1]
	>>> quicksort([1,2])
	[1, 2]
	>>> quicksort([2,1])
	[1, 2]
	>>> quicksort([3,1,2])
	[1, 2, 3]
	>>> quicksort([1, 10 , 9, 15, 2, -1, 12, 4, 100, 101])
	[-1, 1, 2, 4, 9, 10, 12, 15, 100, 101]
	'''
	if len(array) <= 1:
		# Arrays of length 1 or less are by definition sorted
		return array
	else:
		pivot = array[len(array)/2]
		del array[len(array)/2]
		less = list()
		more = list()
		for i in array:
			if i <= pivot:
				less.append(i)
			else:
				more.append(i)
		return quicksort(less) + [pivot] + quicksort(more)


if __name__ == "__main__":
	import doctest
	doctest.testmod()
