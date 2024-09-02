# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def PostOrder(node):
            if node == None:
                return None
            PostOrder(node.left)
            PostOrder(node.right)
            result.append(node.val)
        PostOrder(root)
        return result