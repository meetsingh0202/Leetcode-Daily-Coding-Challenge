# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(currNode):
            if currNode == None:
                return
            
            HashMap[currNode.val] = 1 + HashMap.get(currNode.val, 0)
            
            traverse(currNode.left)
            traverse(currNode.right)
        
        HashMap = dict()
        traverse(root)
        
        l = list(HashMap.keys())
        l.sort(key = lambda x : HashMap[x], reverse = True)
        res = []
        
        res.append(l[0])
        
        for i in l[1:]:
            if HashMap[i] == HashMap[res[0]]:
                res.append(i)
            else:
                break
        
        return res