def findClosestValueInBstHelper(tree, target, _closest):
	if tree is None:
		return _closest
	new_diff = abs(target - tree.value)
	if abs(target - _closest) > new_diff:
		_closest = tree.value
	if tree.value == target:
		return tree.value
	elif target > tree.value and tree.right is not None:
		return findClosestValueInBstHelper(tree.right, target, _closest)
	elif target < tree.value and tree.left is not None:
		return findClosestValueInBstHelper(tree.left, target, _closest)
	return _closest

def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float("inf"))