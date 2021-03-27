def findSum(depth, array):
	product_sum = 0
	for a in array:
		if isinstance(a, int):
			product_sum = product_sum + a
		else:
			product_sum = product_sum + findSum(depth+1,  a)
	return depth * product_sum



def productSum(array):
    product_sum = 0
	for a in array:
		if isinstance(a, int):
			product_sum = product_sum + a
		else:
			product_sum = product_sum + findSum(2, a)
	return product_sum