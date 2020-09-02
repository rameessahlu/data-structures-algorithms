def bubbleSort(array):
	right_p = len(array)
	for x in range(0, len(array)):
		for xx in range(0, right_p-1):
			if(array[xx] > array[xx+1]):
				array[xx], array[xx+1] = array[xx+1], array[xx]
		right_p = right_p - 1
	return array


_list = [5, 8, 2, 4]

print(_list)

print(bubbleSort(_list))