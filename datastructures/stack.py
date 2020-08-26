class Stack:
	
	def __init__(self):
		self._max = 10
		self._stack = []
		self._pointer = -1

	def push(self, val):
		if not self.isFull():
			self._stack.append(val)
			self._pointer += 1
		else:
			print('Can\'t push, Stack is FULL!')

	def pop(self):
		if not self.isEmpty():
			print('Popped {}'.format(self.peek()))
			self._stack.pop()
			self._pointer -= 1
		else:
			print('Can\'t pop, Stack is empty!')		

	def isFull(self):
		if self._max <= len(self._stack):
			return 1
		else:
			return 0

	def isEmpty(self):
		if len(self._stack) == 0:
			return 1
		else:
			return 0

	def peek(self):
		if not self.isEmpty():
			return self._stack[self._pointer]
		else:
			return None

if __name__ == '__main__':
	_stack = Stack()
	_stack.push(10)
	_stack.push(15)
	_stack.push(20)
	print(_stack.peek())
	_stack.push(65)
	_stack.push(50)
	_stack.push(84)
	_stack.pop()
	print(_stack.peek())	