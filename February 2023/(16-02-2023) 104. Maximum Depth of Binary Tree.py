# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def traverse(root):
            if root == None:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            return 1 + max(left, right)
        
        return traverse(root)
