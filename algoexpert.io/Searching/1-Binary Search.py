def BS(left, right, array, target):
	if int( (left+right) % 2 ) == 0:
		mid = int( (left+right) / 2 )
	else:
		mid = int( (left + right + 1) / 2 )
	if array[mid] == target:
		return mid
	if left == right:
		return -1
	if target > array[mid]:
		return BS(mid+1, right, array, target)
	else:
		return BS(left, mid-1, array, target)
	
def binarySearch(array, target):
    l = 0
	r = len(array)-1
	return BS(l, r, array, target)
