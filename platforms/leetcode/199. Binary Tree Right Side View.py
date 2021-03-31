# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.level_to_node_mapping = {}
    
    def rsvHelper(self, root, level, queue):
        if level not in self.level_to_node_mapping:
            self.level_to_node_mapping[level] = [root.val]
        else:
             self.level_to_node_mapping[level].append(root.val)
        
        if root.left != None:
            queue.append([root.left, level+1])
        
        if root.right != None:
            queue.append([root.right,level+1])
        
        if(queue):
            popped = queue.pop(0)
            self.rsvHelper(popped[0], popped[1], queue)
        return
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if  not root:
            return []
        self.rsvHelper(root, 0, [])
        result = []
        for k, v in self.level_to_node_mapping.items():
            result.append(v[-1])
        return result