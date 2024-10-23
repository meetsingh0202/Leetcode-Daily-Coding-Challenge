# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(root, level):
            if root == None:
                return 
            
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
            
            if level <= 2:
                root.val = 0
            else:
                currTotalSum = totalLevelSum[level]
                currParentSum = parentSum[parent[root]]
                root.val = currTotalSum - currParentSum
            
        q = deque([root])
        parent = dict()
        levels = []

        parentSum = dict()
        totalLevelSum = dict()
        currLevel = 0

        while q:
            currLevelSum = 0
            currLevel += 1

            for i in range(len(q)):
                currNode = q.popleft()
                currLevelSum += currNode.val
                sumOfCurrChild = 0

                if currNode.right:
                    parent[currNode.right] = currNode
                    sumOfCurrChild += currNode.right.val
                    q.append(currNode.right)
                    
                if currNode.left:
                    parent[currNode.left] = currNode
                    sumOfCurrChild += currNode.left.val
                    q.append(currNode.left)
                    
                parentSum[currNode] = sumOfCurrChild
            totalLevelSum[currLevel] = currLevelSum
            
        traverse(root, 1)
        return root