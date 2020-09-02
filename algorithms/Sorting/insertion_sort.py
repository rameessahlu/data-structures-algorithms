def insertionSort(array):
    #sorted array pointers
	sa_lp = 0
	sa_rp = 0
	#unsorted array pointers
	usa_lp = 1
	usa_rp = len(array)
	
	for uns in range(usa_lp, usa_rp):
		sa_rp = uns - 1
		for sa in range(uns, sa_lp, -1):
			if array[sa] < array[sa-1]:
				array[sa], array[sa-1] = array[sa-1], array[sa]
	return array


_list = [5, 8, 2, 4]

print(_list)

print(insertionSort(_list))