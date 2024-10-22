# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if root==None:
            return root
        
        queue=[root]
        res=[]
        while queue:
            ans=[]
            l=len(queue)
            for i in range(l):
                temp=queue.pop(0)
                ans.append(temp.val)
                
                if temp.left:
                    queue.append(temp.left)
                    
                if temp.right:
                    queue.append(temp.right)
            
            res.append(ans)
    
        if len(res) < k:
            return -1
        
        Max = 0
        res1 = []
        
        for i in res:
            res1.append(sum(i))
        res1.sort(reverse = True)
        return res1[k - 1]
        