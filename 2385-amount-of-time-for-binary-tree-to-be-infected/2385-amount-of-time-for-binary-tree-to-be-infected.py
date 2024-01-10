# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacent=defaultdict(list)
        stack = [(root, None)]
        while stack: 
            n, p = stack.pop()
            if p: 
                adjacent[p.val].append(n.val)
                adjacent[n.val].append(p.val)
            if n.left: 
                stack.append((n.left, n))
            if n.right: 
                stack.append((n.right, n))
                
        res=-1
        visited={start}
        queue=deque([start])
        while queue:
            lengthofqueue=len(queue)
            for i in range(lengthofqueue):
                temp=queue.popleft()
                for adj in adjacent[temp]:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
            res+=1
        return res