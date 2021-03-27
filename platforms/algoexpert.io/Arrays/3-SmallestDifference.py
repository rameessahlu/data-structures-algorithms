def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	
	lp_firArr = 0
	lp_secArr = 0
	
	result = []
	diff = 9999999999999999
	
	while(True):
		if lp_secArr == len(arrayTwo)-1 and lp_firArr == len(arrayOne)-1:
			if diff > abs(arrayOne[lp_firArr] - arrayTwo[lp_secArr]):
				result = [arrayOne[lp_firArr], arrayTwo[lp_secArr]]
				diff = abs(arrayOne[lp_firArr] - arrayTwo[lp_secArr])
			break

		if (arrayOne[lp_firArr] - arrayTwo[lp_secArr]) == 0:
			return [ arrayOne[lp_firArr], arrayTwo[lp_secArr] ]
		else:				
			if diff > abs(arrayOne[lp_firArr] - arrayTwo[lp_secArr]):
				result = [arrayOne[lp_firArr], arrayTwo[lp_secArr]]
				diff = abs(arrayOne[lp_firArr] - arrayTwo[lp_secArr])
			
			if arrayOne[lp_firArr] >  arrayTwo[lp_secArr]:
				if lp_secArr != len(arrayTwo)-1:
					lp_secArr+= 1
				elif lp_firArr != len(arrayOne)-1:
					lp_firArr+= 1
			else:
				if lp_firArr != len(arrayOne)-1:
					lp_firArr+= 1
				elif lp_secArr != len(arrayTwo)-1:
					lp_secArr+= 1
	return result