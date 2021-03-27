def threeNumberSum(array, targetSum):
	array.sort()
    result = []
	for a in range(0, len(array)-1): 
		lp = a+1
		rp = len(array)-1
		while(True):
			if lp == rp:
				break
			temp_sum = array[a] + array[lp] + array[rp]
			if temp_sum  ==  targetSum:
				result.append([array[a], array[lp], array[rp]])
			if targetSum > temp_sum:
				lp = lp + 1
			else:
				rp = rp - 1
	return result