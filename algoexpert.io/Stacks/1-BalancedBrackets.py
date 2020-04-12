def balancedBrackets(string):
    stack = []
	_dic = { '(' : ')', '[': ']', '{' : '}' }
	_reverse_dic = { ')' : '(', ']': '[', '}' : '{' }
	for s in string:
		#print(stack)
		if not stack:
			stack.append(s)
			continue
		if stack[len(stack)-1] in _dic:
			if s in _dic:
				stack.append(s)
				continue
			if s in _reverse_dic and _reverse_dic[s] == stack[len(stack)-1]:
				stack.pop()
			else:
				return False
		else:
			stack.append(s)
	if not stack:
		return True
	else:
		return False