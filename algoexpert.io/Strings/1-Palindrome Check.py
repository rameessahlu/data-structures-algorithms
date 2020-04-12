def isPalindrome(string):
	right_p = len(string)-1
	for x in range(0, int(len(string)/2)):
		if string[right_p] !=  string[x]:
			return False
		right_p = right_p - 1
	return True
			