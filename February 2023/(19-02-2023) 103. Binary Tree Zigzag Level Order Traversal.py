# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lvl_order=[]
        q= collections.deque()
        q.append(root)
        while q:
            lvl=[]
            for i in range(len(q)):
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvl.append(curr.val)
            lvl_order.append(lvl)
        for i in range(len(lvl_order)):
            if i%2== 1:
                lvl_order[i]= lvl_order[i][::-1]
        return lvl_order
