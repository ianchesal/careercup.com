'''
mergesort

Sort arrays using the mergesort approach to sorting. For example:

>>> mergesort([2,1])
[1, 2]
>>> mergesort([4,5,3,1])
[1, 3, 4, 5]

'''

def mergesort(array):
	'''
	Sorts an array using the mergesort algorithm. Returns the sorted
	array.

	>>> mergesort([])
	[]
	>>> mergesort([1])
	[1]
	>>> mergesort([1,2])
	[1, 2]
	>>> mergesort([2,1])
	[1, 2]
	>>> mergesort([3,1,2])
	[1, 2, 3]
	>>> mergesort([1, 10 , 9, 15, 2, -1, 12, 4, 100, 101])
	[-1, 1, 2, 4, 9, 10, 12, 15, 100, 101]
	'''
	if len(array) <= 1:
		return array
	else:
		return _merge(mergesort(array[:len(array)/2]), mergesort(array[len(array)/2:]))

def _merge(left, right):
	'''
	Merges two *sorted* arrays, left and right, according to the mergesort
	merge approach and returns the *sorted* merged array. Arrays do not need
	to be equal length.

	>>> _merge([], [])
	[]
	>>> _merge([1], [1])
	[1, 1]
	>>> _merge([1], [2])
	[1, 2]
	>>> _merge([2], [1])
	[1, 2]
	>>> _merge([1, 2], [3])
	[1, 2, 3]
	>>> _merge([3], [1,2])
	[1, 2, 3]
	>>> _merge([1,4], [2,3])
	[1, 2, 3, 4]
	>>> _merge([], [1, 2])
	[1, 2]
	'''
	left_index = 0
	right_index = 0
	merged_array = list()
	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			merged_array.append(left[left_index])
			left_index = left_index + 1
		elif left[left_index] > right[right_index]:
			merged_array.append(right[right_index])
			right_index = right_index + 1
		else:
			merged_array.append(left[left_index])
			merged_array.append(right[right_index])
			left_index = left_index + 1
			right_index = right_index + 1
	# If the arrays are not equal length there might be some
	# stuff left over in one of them. Drain the remaining stuff
	# in to the merged array.
	if left_index < len(left):
		merged_array = merged_array + left[left_index:]
	elif right_index < len(right):
		merged_array = merged_array + right[right_index:]
	return merged_array

if __name__ == "__main__":
	import doctest
	doctest.testmod()
