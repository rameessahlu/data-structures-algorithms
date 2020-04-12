def findFib(f, s, n):
	if n == 0:
		return s
	t = f
	f = s
	s = t+s
	n = n - 1
	return findFib(f, s, n)

def getNthFib(n):
	if n == 1:
		return 0
    return findFib(0, 1, n-2)
