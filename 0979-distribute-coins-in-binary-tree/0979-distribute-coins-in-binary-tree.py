# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            nonlocal count
            
            if root==None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            count += abs(left) + abs(right)
            return root.val + left + right - 1
        
        count = 0
        traverse(root)
        return count
    