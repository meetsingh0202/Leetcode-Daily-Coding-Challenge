# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def traverse(currRoot, currStr):
            
            if currRoot == None:
                return ""
            
            if currRoot.left == None and currRoot.right == None:
                return (currStr + chr(97 + currRoot.val))[::-1]
            
            left = traverse(currRoot.left, currStr + chr(97 + currRoot.val))
            right = traverse(currRoot.right, currStr + chr(97 + currRoot.val))
            
            if left == "":
                return right
            
            if right == "":
                return left
            
            return min(left, right)
        
        return traverse(root, "")