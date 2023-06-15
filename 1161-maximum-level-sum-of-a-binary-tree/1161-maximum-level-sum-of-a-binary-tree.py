# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = []
        
        queue = deque([root])
        maxSum = float('-inf')
        level = 0
        res = 0
        
        while queue:
            currSum = 0
            level += 1
            for i in range(len(queue)):
                currNode = queue.popleft()
                currSum += currNode.val
                
                if currNode.right:
                    queue.append(currNode.right)
                
                if currNode.left:
                    queue.append(currNode.left)
            
            if currSum > maxSum:
                maxSum = max(maxSum, currSum)
                res = level
        
        return res