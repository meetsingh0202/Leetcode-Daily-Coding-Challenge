# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if root == None:
                return 0
            
            if root.left == None and root.right == None:
                return 1
            
            minDepth = float('inf')
            
            if root.left != None:
                minDepth = min(minDepth, traverse(root.left))
            
            if root.right != None:
                minDepth = min(minDepth, traverse(root.right))
            
            return 1 + minDepth
        
        return traverse(root)