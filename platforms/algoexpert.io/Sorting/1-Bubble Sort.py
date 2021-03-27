def bubbleSort(array):
	right_p = len(array)
    for x in range(0, len(array)):
		for xx in range(0, right_p-1):
			if(array[xx] > array[xx+1]):
				temp = array[xx]
				array[xx] = array[xx+1]
				array[xx+1] = temp
		right_p = right_p - 1
	return array