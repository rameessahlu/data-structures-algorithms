
class Node:
	def __init__(self, data):
		self._data = data
		self._prev = None
		self._next = None

class DoublyLinkedList:
	def __init__(self):
		self._head = None
		self._tail = None

	def insert_at_the_beginning(self, data):
		if self._head == None:
			self._head = Node(data)
			self._tail = self._head
			return
		temp_n = Node(data)
		temp_n._next = self._head
		self._head._prev = temp_n
		self._head = temp_n

	def insert_after(self, prev, data):
		if self._head == None:
			print('list is empty.')
			return
		temp_n = self._head
		while (temp_n != None):
			if temp_n._data == prev:
				new_node = Node(data)
				post_node = temp_n._next
				
				temp_n._next = new_node
				new_node._prev = temp_n

				new_node._next = post_node

				if post_node == None:
					self._tail = new_node
				else:
					post_node.prev = temp_n
				return
			temp_n = temp_n._next
		print('there\'s no node exist with data {} to insert after it.'.format(prev))

	def insert_at_the_end(self, data):
		if self._head == None:
			self._head = Node(data)
			return
		new_node = Node(data)
		self._tail._next = new_node
		new_node._prev = self._tail
		self._tail = new_node

	def print_list_asc(self):
		if self._head == None:
			print('list is empty.')
			return
		temp_n = self._head
		while (temp_n != None):
			print(temp_n._data)
			temp_n = temp_n._next

	def print_list_desc(self):
		if self._head == None or self._tail is None:
			print('list is empty.')
			return
		temp_n = self._tail
		while (temp_n != None):
			print(temp_n._data)
			temp_n = temp_n._prev

	def delete_node_by_value(self, data):
		temp_n = self._head

		if self._head == None:
			print('list is empty.')
			return

		if temp_n._data == data:
			self._head = self._head._next
			if self._head is None:
				self._tail = self._head
			return

		while (temp_n._next != None):
			if temp_n._next._data == data:
				break
			temp_n = temp_n._next

		if temp_n._next == None:
			print('data not present in the list.')
			return
		else:
			pre_node = temp_n
			post_node = temp_n._next._next
			
			pre_node._next = post_node
			if post_node is not None:
				post_node._prev = pre_node
			else:
				self._tail = pre_node

	def delete_node_by_position(self, pos):
		temp_n = self._head

		if self._head == None:
			print('list is empty.')
			return

		if pos == 0:
			post_node = self._head._next
			if post_node is not None:
				self._head = post_node
				post_node._prev = None
			return

		_index = 0
		while (temp_n._next != None):
			if pos == _index-1:
				break
			_index += 1
			temp_n = temp_n._next

		if temp_n.next == None:
			print('position is out of range.')
			return
		else:
			pre_node = temp_n
			post_node = temp_n._next._next

			pre_node._next = post_node
			if post_node is not None:
				post_node._prev = pre_node
			else:
				self._tail = pre_node

if __name__ == '__main__':
	_linked_list = DoublyLinkedList()
	_linked_list.insert_at_the_beginning(10)
	_linked_list.insert_at_the_end(20)
	_linked_list.insert_at_the_end(35)
	_linked_list.insert_at_the_end(58)
	_linked_list.insert_at_the_end(73)
	_linked_list.insert_at_the_end(99)
	_linked_list.insert_after(20, 88)
	_linked_list.print_list_asc()
	print('----------------------')
	_linked_list.delete_node_by_value(88)
	_linked_list.delete_node_by_position(0)
	_linked_list.print_list_desc()