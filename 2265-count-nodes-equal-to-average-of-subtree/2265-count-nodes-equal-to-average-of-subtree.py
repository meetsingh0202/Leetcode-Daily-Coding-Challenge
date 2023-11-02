# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(currNode):
            if currNode == None:
                return [0, 0]
            
            leftSum, leftCount = traverse(currNode.left)
            rightSum, rightCount = traverse(currNode.right)
            
            currCount = leftCount + rightCount + 1
            currSum = leftSum + rightSum + currNode.val
            
            currAvg = currSum // currCount
            
            if currAvg == currNode.val:
                self.count += 1
                
            return currSum, currCount
                
        self.count = 0
        traverse(root)
        return self.count