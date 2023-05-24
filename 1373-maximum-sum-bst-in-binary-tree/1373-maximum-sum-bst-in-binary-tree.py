# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        
        def traverse(root):
            if root == None:
                return 0, float('-inf'), float('inf')
            
            if root.left == None and root.right == None:
                return root.val, root.val, root.val
            
            leftSum, leftMax, leftMin = traverse(root.left)
            rightSum, rightMax, rightMin = traverse(root.right)
            
            currVal = root.val
            
            # print(root.val)
            # print(leftSum, leftMax, leftMin)
            # print(rightSum, rightMax, rightMin)
            # print("---------------------------------")
            
            if root.right and root.left:
                if leftMax < rightMin and leftMax < root.val and rightMin > root.val:
                    self.max = max(self.max, root.val + leftSum + rightSum)
                    return root.val + leftSum + rightSum, rightMax, leftMin
                else:
                    if rightMax != float("inf") and leftMax != float('inf'):
                        self.max = max(self.max, leftSum, rightSum)
                    elif rightMin > currVal and root.right.val > root.val:
                        self.max = max(self.max, rightSum)
                    elif leftMax < currVal and root.left.val < root.val:
                        self.max = max(self.max, leftSum)
                
            else:
                if root.right and rightMin > root.val:
                    self.max = max(self.max, root.val + rightSum)
                    return root.val + rightSum, rightMax, currVal
                
                if root.left and leftMax < root.val:
                    self.max = max(self.max, root.val + leftSum)
                    return root.val + leftSum, currVal, leftMin
                
            return root.val, float('inf'), float('-inf')

                
        traverse(root)
        return self.max