# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumsHelperFn(root, prvSum, array):
	if root.left == None and root.right == None:
		array.append(prvSum+root.value)
	if root.left != None:
		branchSumsHelperFn(root.left, prvSum+root.value, array)
	if root.right != None:
		branchSumsHelperFn(root.right, prvSum+root.value, array)
	return array
def branchSums(root):
    return branchSumsHelperFn(root, 0,[])
