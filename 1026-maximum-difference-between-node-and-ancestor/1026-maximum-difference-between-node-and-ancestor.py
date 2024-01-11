# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traverse(currNode, minVal, maxVal):
            
            if currNode == None:
                return 0
            
            currVal = currNode.val
            
            left = traverse(currNode.left, min(minVal, currVal), max(maxVal, currVal))
            right = traverse(currNode.right, min(minVal, currVal), max(maxVal, currVal))
            
            diff1, diff2 = float('-inf'), float('-inf')
            
            if minVal != float('inf'):
                diff1 = abs(currVal - minVal)
            
            if maxVal != float('-inf'):
                diff2 = abs(currVal - maxVal)
            
            return max(diff1, diff2, left, right)
        
        return traverse(root, float('inf'), float('-inf'))