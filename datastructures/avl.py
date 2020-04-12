class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

class AVLTree:
	def __init__(self):
		self.root = None

	def inOrder(self, root):
		if root.left != None:
			self.inOrder(root.left)
		print('{}.w({})'.format(root.val, root.height))
		if root.right != None:
			self.inOrder(root.right)

	def display(self):
		temp_r = self.root
		self.inOrder(temp_r)

	def getHeight(self, node):
		if not node:
			return 0
		else:
			return	node.height

	def getBalanceFactor(self, node):
		if not node:
			return 0
		else:
			return self.getHeight(node.left) - self.getHeight(node.right) #height of left subtree - height of right subtree

	def leftRotate(self, node):
		new_root = node.right
		sub_right_left = node.right.left

		new_root.left = node
		node.right = sub_right_left

		#update_weights
		new_root.left.height = 1 + max(self.getHeight(new_root.left.left), self.getHeight(new_root.left.right))
		new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))

		return new_root

	def rightRotate(self, node):
		new_root = node.left
		sub_left_right = new_root.right

		new_root.right = node
		node.left = sub_left_right

		#update_weights
		new_root.right.height = 1 + max(self.getHeight(new_root.right.left), self.getHeight(new_root.right.right))
		new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))

		return new_root

	def insertionHelper(self, root, val):
		if root == None:
			return Node(val)
		#bst insertion
		if root.val > val:
			if root.left != None:
				root.left = self.insertionHelper(root.left, val)
			else:
				root.left = Node(val)
		elif root.val < val:
			if root.right != None:
				root.right = self.insertionHelper(root.right, val)
			else:
				root.right = Node(val)

		#update weight		
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

		balance_factor = self.getBalanceFactor(root)
		#if the node is unbalnced
		#1: Left Left Case
		if balance_factor > 1 and val < root.left.val:
			return self.rightRotate(root)
         
		 #2 - Left Right Case 
		if balance_factor > 1 and val > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		#3 - Right Right Case 
		if balance_factor < -1 and val > root.right.val: 
			return self.leftRotate(root) 
  
		#4 - Right Left Case 
		if balance_factor < -1 and val < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 
		return root

	def insert(self, val):
		self.root = self.insertionHelper(self.root, val)

	def findHeighestInorderPredecessor(self, root, highest):
		if highest < root.val:
			highest = root.val
		if root.left is not None:
			return self.findHeighestInorderPredecessor(root.left, highest)
		if root.right is not None:
			return self.findHeighestInorderPredecessor(root.right, highest)
		return highest

	def deletionHelper(self, root, val):
		if root == None:
			return root
		#bst insertion
		if root.val > val:
			if root.left != None:
				root.left = self.deletionHelper(root.left, val)
		elif root.val < val:
			if root.right != None:
				root.right = self.deletionHelper(root.right, val)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			else:
				#highest inorder predecessor deletion
				temp = self.findHeighestInorderPredecessor(root.left, root.left.val)
				root.val = temp
				root.left = self.deletionHelper(root.left, temp)
				
				#lowest inorder successor deletion
				#temp = self.findLowestInorderSuccessor(root.right, highest)
				#root.val = temp.val
				#root.right = self.deletionHelper(root, temp.val)

		#update weight		
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

		balance_factor = self.getBalanceFactor(root)
		#if the node is unbalnced
		#1: Left Left Case
		if balance_factor > 1 and self.getBalanceFactor(root.left) >= 0:
			return self.rightRotate(root)
         
		 #2 - Left Right Case 
		if balance_factor > 1 and self.getBalanceFactor(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		#3 - Right Right Case 
		if balance_factor < -1 and self.getBalanceFactor(root.right) >= 0: 
			return self.leftRotate(root) 
  
		#4 - Right Left Case 
		if balance_factor < -1 and self.getBalanceFactor(root.left) < 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 
		return root

	def delete(self, val):
		self.root = self.deletionHelper(self.root, val)

if __name__ == '__main__':
	avl = AVLTree()
	avl.insert(30)
	avl.insert(5)
	avl.insert(35)
	avl.insert(32)
	avl.insert(40)
	avl.display()
	print('------')
	avl.insert(45)
	avl.display()
	print('------')
	avl.delete(30)
	avl.display()