a = 727
b = 0
o = a

while (a != 0):
	b = (b* 10) + (a % 10)
	a = int(a /10)

if o == b:
	print('its a palindrome')
else:
	print('not a palindrome')