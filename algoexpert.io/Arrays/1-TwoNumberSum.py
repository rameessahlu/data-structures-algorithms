def twoNumberSum(array, targetSum):
    temp_list = []
	for x in array:
		if (targetSum - x) not in temp_list:
			temp_list.append(x)
		else:
			result_list = [x, (targetSum-x)]
			result_list.sort()
			return result_list
	return []