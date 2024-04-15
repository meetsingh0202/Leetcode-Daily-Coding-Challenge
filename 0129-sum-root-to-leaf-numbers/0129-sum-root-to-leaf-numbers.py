# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(root,arr,ans):
            if not root:
                return 
            arr.append(str(root.val))
            if root.left==None and root.right==None:
                ans.append(arr.copy())
                # print(arr)
                arr.pop()
                return
            path(root.left,arr,ans)
            path(root.right,arr,ans)
            del arr[-1]
        
        arr=[]
        ans=[]
        path(root,arr,ans)
        sum1=0
        for i in ans:
            # print(i)
            temp="".join(i)
            sum1+=int(temp)
        return sum1