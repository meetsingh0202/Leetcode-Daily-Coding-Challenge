# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        res = []
        
        def traverse(currNode):
            if not currNode:
                return None
            
            currNode.left = traverse(currNode.left)
            currNode.right = traverse(currNode.right)
			
            if currNode.val in to_delete:
                
                if currNode.left:
                    res.append(currNode.left)
                
                if currNode.right:
                    res.append(currNode.right)
            
                return None

            return currNode
                
        traverse(root)
        
        if root.val not in to_delete:
            res.append(root)

        return res
