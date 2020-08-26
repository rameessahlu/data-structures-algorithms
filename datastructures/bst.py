
class Node:
	def __init__(self, val):
		self._left = None
		self._right = None
		self._key = val

class BST:
	def __init__(self):
		self._root = None

	def insert_helper(self, root, val):
		if root is None:
			return Node(val)

		if val < root._key:
			root._left = self.insert_helper(root._left, val)
		elif val > root._key:
			root._right = self.insert_helper(root._right, val)

		return root

	def insert(self, val):
		self._root = self.insert_helper(self._root, val)

	def preorder_traversal(self):
		pass

	def inorder_traversal(self, root):
		if root._left is not None:
			self.inorder_traversal(root._left)
		print(root._key)
		if root._right is not None:
			self.inorder_traversal(root._right)		

	def postorder_traversal(self):
		pass

	def min_value_node(self):
		if self._root is None:
			print('BST is empty.')
			return
		temp_root = self._root

		while True:
			if temp_root._left is not None:
				temp_root = temp_root._left
			else:
				break
		print('Min value node is {}'.format(temp_root._key))

	def find_lowest_val_in_right_hand(self, root):
		if root is not None:
			return self.find_lowest_val_in_right_hand(root._right)
		else:
			return root._key

	def delete_helper(self, root, val):
		if root is None:
			return Node(val)

		if val == root._key:
			if root._left is not None and root._right is not None:
				root._key = self.find_lowest_val_in_right_hand(root._right)
				root._right = self.delete_helper(root._right, root._key)
			else:
				return None
		elif val < root._key:
			root._left = self.delete_helper(root._left, val)
		elif val > root._key:
			root._right = self.delete_helper(root._right, val)

		return root

	def delete_node(self, val):
		self._root = self.delete_helper(self._root, val)

if __name__ == '__main__':
	_bst = BST()
	_bst.insert(15)
	_bst.insert(20)
	_bst.insert(65)
	_bst.insert(10)
	_bst.insert(50)
	_bst.insert(84)
	_bst.min_value_node()
	_bst.inorder_traversal(_bst._root)
	
	print('--------------------------')

	_bst.delete_node(10)
	_bst.min_value_node()	
	_bst.inorder_traversal(_bst._root)