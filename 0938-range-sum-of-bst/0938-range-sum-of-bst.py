# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(root):
            if root == None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if low <= root.val <= high:
                return root.val + left + right
            return left + right
        return traverse(root)
                 