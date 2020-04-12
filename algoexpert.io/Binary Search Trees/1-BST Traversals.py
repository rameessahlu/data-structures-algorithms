class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

# def preOrderTraverse(tree, array):
#     stack = []
#     while(tree.left is not None):
#     	stack.append(tree)
#     	tree = tree.left
#     stack.append(tree)

#     for i in range(len(stack)-1, -1, -1):
#     	print(i)
#     	array.append(stack[i].value)
#     	if stack[i].right is not None:
#     		array.append(stack[i].right.value)
#     return array

def preOrderTraverse(tree, array):
	array.append(tree.value)
	if tree.left is not None:
		preOrderTraverse(tree.left, array)
	if tree.right is not None:
		preOrderTraverse(tree.right, array)
	return array

def inOrderTraverse(tree, array):
	if tree.left is not None:
		inOrderTraverse(tree.left, array)
	array.append(tree.value)
	if tree.right is not None:
		inOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array):
	if tree.left is not None:
		postOrderTraverse(tree.left, array)
	if tree.right is not None:
		postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array




if __name__ == '__main__':
    test = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
    print(inOrderTraverse(test, []))
    print(postOrderTraverse(test, []))
    print(preOrderTraverse(test, []))
'''
    array.append(tree.value);
    if tree.left is None:
        return 
    preOrderTraverse(tree.left, arrray);
    preOrderTraverse(tree.right, arrray);
'''