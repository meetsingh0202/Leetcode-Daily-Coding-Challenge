# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def traverse(currNode, prev):
            if currNode == None:
                return 0
            
            currVal = currNode.val   
            
            leftScore = traverse(currNode.left, currVal)
            rightScore =  traverse(currNode.right, currVal)
            
            self.ans = max(self.ans, leftScore + rightScore)
            
            if currVal == prev:
                return 1 + max(leftScore, rightScore) 
            
            return 0
        
        self.ans = 0
        traverse(root, None)
        return self.ans