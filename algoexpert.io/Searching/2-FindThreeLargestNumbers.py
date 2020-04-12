def shiftingAndInsertion(result, newNumber):
	if result[2] < newNumber:
		temp2 = result[2]
		result[2] = newNumber
		temp1 = result[1]
		result[1] = temp2
		result[0] = temp1
	elif result[1] < newNumber:
		temp = result[1]
		result[1] = newNumber
		result[0] = temp
	elif result[0] < newNumber:
		result[0] = newNumber
def findThreeLargestNumbers(array):
    result = []
	for i in range(0, len(array)):
		if not result:
			result.append(array[i])
			continue
		if len(result) is 1:
			result.append(array[i])
			if result[0] > result[1]:
				temp = result[1]
				result[1] = result[0]
				result[0] = temp
			continue
		if len(result) is 2:
			result.append(array[i])
			if result[1] > result[2]:
				temp = result[2]
				result[2] = result[1]
				result[1] = temp
			if result[0] > result[1]:
				temp = result[1]
				result[1] = result[0]
				result[0] = temp
			continue
		shiftingAndInsertion(result, array[i])
	return result