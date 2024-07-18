# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        parent = dict()
        leafNodes = set()
        
        def findParent(currNode):
            if currNode == None:
                return 
            
            if currNode.left == None and currNode.right == None:
                leafNodes.add(currNode)
                return 
            
            if currNode.left:
                parent[currNode.left] = currNode
                findParent(currNode.left)
                
            if currNode.right:
                parent[currNode.right] = currNode
                findParent(currNode.right)
            
        findParent(root)
        
        def traverse(currNode, currDistance, prev):
            nonlocal count
            
            if currDistance > 0 and currNode.left == None and currNode.right == None:
                count += 1
            
            if parent.get(currNode, []):
                if currDistance + 1 <= distance and parent.get(currNode) != prev:
                    traverse(parent.get(currNode), currDistance + 1, currNode)
            
            if currNode.left and currNode.left != prev:
                if currDistance + 1 <= distance:
                    traverse(currNode.left, currDistance + 1, currNode)

            if currNode.right and currNode.right != prev:
                if currDistance + 1 <= distance:
                    traverse(currNode.right, currDistance + 1, currNode)
            
        count = 0
        for i in leafNodes:
            traverse(i, 0, i)
            
        return count // 2