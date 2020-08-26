class Queue:
	
	def __init__(self):
		self._max = 10
		self._Q = []
		self._front = -1
		self._rear = -1
		self._size = 0

	def enqueue(self, val):
		if not self.isFull():
			self._Q.append(val)
			if self.isEmpty():
				self._front += 1
			self._rear += 1
			self._size += 1
		else:
			print('Can\'t enqueue, Queue is FULL!')

	def dequeue(self):
		if not self.isEmpty():
			self._front += 1
			if self._rear < self._front:
				self._front = -1
				self._rear = -1

			self._size -= 1
		else:
			print('Can\'t dequeue, Queue is empty!')		

	def isFull(self):
		if self._size >= self._max-1:
			return 1
		else:
			return 0

	def isEmpty(self):
		if self._rear is -1 or self._front is -1 or self._size == 0:
			return 1
		else:
			return 0

	def retrieve_front(self):
		if self.isEmpty():
			print('Queue is empty!')
		else:
			print('Front: {}'.format(self._Q[self._front]))

	def retrieve_rear(self):
		if self.isEmpty():
			print('Queue is empty!')
		else:
			print('Rear: {}'.format(self._Q[self._rear]))


if __name__ == '__main__':
	_queue = Queue()
	_queue.enqueue(10)
	_queue.enqueue(15)
	_queue.enqueue(20)
	_queue.retrieve_front()
	_queue.retrieve_rear()
	_queue.enqueue(65)
	_queue.enqueue(50)
	_queue.enqueue(84)
	_queue.dequeue()
	_queue.retrieve_front()
	_queue.retrieve_rear()