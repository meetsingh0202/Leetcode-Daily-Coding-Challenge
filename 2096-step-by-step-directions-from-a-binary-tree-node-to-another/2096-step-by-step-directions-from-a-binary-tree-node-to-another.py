# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def startTraverse(currRoot, path, target):
            
            while currRoot != target:
                currRoot = parent[currRoot][0]
                path += 'U'
            
            return path
                
        def destTraverse(currRoot, path, target):

            while currRoot != target:
                if parent[currRoot][1]:
                    path += "L"
                else:
                    path += "R"
                    
                currRoot = parent[currRoot][0]
            
            return path
                    
        def findLca(root):
            if root == None or root.val == startValue or root.val == destValue:
                return root
            
            left = findLca(root.left)
            right = findLca(root.right)
            
            if left == None:
                return right
            
            if right == None:
                return left
            
            return root      
        
        def findParent(root):
            if root == None:
                return 
            
            findParent(root.right)
            findParent(root.left)
            
            if root.left:
                parent[root.left.val] = [root.val, 1]
            
            if root.right:
                parent[root.right.val] = [root.val, 0]
            
        lca = findLca(root)
        parent = dict()
        findParent(root)
        
        a = startTraverse(startValue, "", lca.val)
        b = destTraverse(destValue, "", lca.val)
        
        return a + b[::-1]