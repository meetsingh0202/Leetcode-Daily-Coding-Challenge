# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check(HashMap):
            oddFlag = False
            
            for key,val in HashMap.items():
                if val%2==1:
                    if oddFlag:
                        return False
                    oddFlag = True
            return True
                
            
            
        def traverse(root, HashMap):
            nonlocal count
            if root:
                HashMap[root.val] = 1 +HashMap.get(root.val,0)
                if root.left == None and root.right == None:
                    if check(HashMap):
                        count+=1
                    HashMap[root.val]-=1
                    if HashMap[root.val]==0:
                        del HashMap[root.val]
                    return
                
                traverse(root.left, HashMap)
                traverse(root.right, HashMap)
                HashMap[root.val]-=1
                if HashMap[root.val]==0:
                    del HashMap[root.val]
        HashMap = dict()
        allPath = []
        count = 0
        traverse(root, HashMap)
        return count