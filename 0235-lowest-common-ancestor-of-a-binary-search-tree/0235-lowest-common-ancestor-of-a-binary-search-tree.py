# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        @cache
        def traverse(root):
            if root == None or root == p or root == q:
                return root
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            if left == None:
                return right
            
            if right == None:
                return left
            
            return root
        
        return traverse(root)