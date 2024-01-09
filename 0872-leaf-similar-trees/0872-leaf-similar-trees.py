# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getSequence(root, currSequence):
            if root == None:
                return currSequence
            left = getSequence(root.left, currSequence)
            right = getSequence(root.right, currSequence)
            currS = left + right
            if root.right == None and root.left == None:
                currS.append(root.val)
                return currS
            return currS
        
        if getSequence(root1, []) == getSequence(root2, []):
            return True
        return False
