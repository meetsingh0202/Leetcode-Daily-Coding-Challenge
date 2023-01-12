# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(root):
            nonlocal res
            if not root:
                return 
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        res = []
        traverse(root)
        return res
