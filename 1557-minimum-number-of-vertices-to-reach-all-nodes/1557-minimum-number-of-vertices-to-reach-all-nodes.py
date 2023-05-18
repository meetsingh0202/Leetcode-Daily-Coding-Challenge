class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = dict()
        
        for i in edges:
            x, y = i
            indegree[y] = 1 + indegree.get(y, 0)
        
        res = []
        for i in range(n):
            if i not in indegree:
                res.append(i)
        return res