def selectionSort(array):
	#unsorted array pointers
	lp = 0
	rp = len(array)
	
	for pp in range(lp, rp):
		#iteration through the unsorted arrray or right portion
		min = pp
		for p in range(pp, rp):
			#selection
			if array[min] > array[p]:
				min = p
		#swapping
		temp = array[min]
		array[min] = array[pp]
		array[pp] = temp
	return array
