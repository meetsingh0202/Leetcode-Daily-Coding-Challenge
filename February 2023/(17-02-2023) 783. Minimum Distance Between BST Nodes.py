# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if root == None:
                return 
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
    
        res = []
        minVal = float('inf')
        traverse(root)
        for i in range(len(res) - 1):
            minVal = min(minVal, abs(res[i] - res[i + 1]))
        return minVal
