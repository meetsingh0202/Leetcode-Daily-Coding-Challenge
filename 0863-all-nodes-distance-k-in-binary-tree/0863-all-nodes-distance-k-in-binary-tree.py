# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent = dict()

        def traverse(root):
            if root == None:
                return 
            
            if root == target:
                q.append([root, 0])
                
            if root.left:
                parent[root.left] = root
            if root.right:
                parent[root.right] = root
            traverse(root.left)
            traverse(root.right)
            
        q = deque([])
        traverse(root)
        res = []
        visited = set()
        
        while q:
            currNode, currDistance = q.popleft()
            
            if currDistance == k:
                res.append(currNode.val)
                continue
                
            visited.add(currNode)
        
            if currNode != root and parent[currNode] not in visited:
                q.append([parent[currNode], currDistance + 1])
            
            if currNode.right and currNode.right not in visited:
                q.append([currNode.right, currDistance + 1])
            
            if currNode.left and currNode.left not in visited:
                q.append([currNode.left, currDistance + 1])
        
        return res
        
