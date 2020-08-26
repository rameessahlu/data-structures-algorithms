
class Node:
	def __init__(self, data):
		self._data = data
		self._next = None

class CircularLinkedList:
	def __init__(self):
		self._last = None

	#fn for empty list as well
	def insert_at_the_beginning(self, data):
		if self._last == None:
			self._last = Node(data)
			self._last._next = self._last
			return
		new_node = Node(data)
		first_node = self._last._next

		new_node._next = first_node
		self._last._next = new_node

	def insert_after(self, prev, data):
		if self._last == None:
			print('list is empty.')
			return
		temp_node = self._last._next #first node
		while (temp_node != self._last):
			if temp_node._data == prev:
				new_node = Node(data)
				post_node = temp_node._next
				temp_node._next = new_node
				new_node._next = post_node
				return
			temp_node = temp_node._next
		print('there\'s no node exist with data {} to insert after it.'.format(prev))

	def insert_at_the_end(self, data):
		if self._last == None:
			self._last = Node(data)
			self.last._next = self._last
			return
		first_node = self._last._next
		new_node = Node(data)
		
		self._last._next = new_node
		new_node._next = first_node

		self._last = new_node

	def print_list_asc(self):
		if self._last == None:
			print('list is empty.')
			return
		temp_n = self._last._next
		while (temp_n != self._last):
			print(temp_n._data)
			temp_n = temp_n._next
		print(temp_n._data)

	def delete_node_by_value(self, data):
		temp_n = self._last._next

		if self._last == None:
			print('list is empty.')
			return

		while (temp_n != self._last):
			if temp_n._next._data == data:
				break
			temp_n = temp_n._next

		if temp_n == self._last and temp_n._next._data != data:
			print('data not present in the list.')
			return
		else:
			pre_node = temp_n
			post_node = temp_n._next._next
			if pre_node._next == self._last:
				self._last =  pre_node
			pre_node._next = post_node

	def delete_node_by_position(self, pos):
		temp_n = self._last._next

		if self._last == None:
			print('list is empty.')
			return

		if pos == 0:
			self._last._next = self._last._next._next
			return

		_index = 0
		while (temp_n != self._last):
			if pos == _index:
				break
			_index += 1
			temp_n = temp_n._next

		if temp_n._next == self._last and pos != _index:
			print('position is out of range.')
			return
		else:
			pre_node = temp_n
			post_node = temp_n._next._next
			if self._last == pre_node._next:
				self._last = pre_node
				print('yes')
			pre_node._next = post_node

if __name__ == '__main__':
	_linked_list = CircularLinkedList()
	_linked_list.insert_at_the_beginning(10)
	_linked_list.insert_at_the_end(20)
	_linked_list.insert_at_the_end(35)
	_linked_list.insert_at_the_end(58)
	_linked_list.insert_at_the_end(73)
	_linked_list.insert_at_the_end(99)
	_linked_list.insert_after(20, 88)
	_linked_list.print_list_asc()
	print('----------------------')
	print(_linked_list._last._data)
	print('----------------------')
	_linked_list.delete_node_by_value(88)
	_linked_list.print_list_asc()
	print('----------------------')
	print(_linked_list._last._data)
	print('----------------------')
	_linked_list.delete_node_by_position(0)
	_linked_list.print_list_asc()