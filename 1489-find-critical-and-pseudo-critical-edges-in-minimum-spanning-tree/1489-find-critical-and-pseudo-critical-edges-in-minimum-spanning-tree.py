class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def find(u):
            if parent[u] == u:
                return u
            return find(parent[u])
            
        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                parent[p1] = p2
        
        def mst(n, edges, include = [], exclude = []):            
            for i in range(n):
                parent[i] = i
            
            cost = 0
            
            if include != []:
                p1 = find(include[0])
                p2 = find(include[1])
                union(p1, p2)
                cost += include[2]
                
            for i in edges:
                if i == exclude or i == include:
                    continue
                    
                u, v, c = i
                
                p1 = find(u)
                p2 = find(v)
                
                if p1 != p2:
                    union(p1, p2)
                    cost += c
            return cost
            
        edges1 = edges[:]
        edges1.sort(key = lambda x : x[2])
        parent = [-1] * n
        originalCost = mst(n, edges1)
        
        res = [[], []]
        
        for i in range(len(edges)):
            includedCost = mst(n, edges1, edges[i], [])
            excludedCost = mst(n, edges1, [], edges[i])
            
            if excludedCost > originalCost or excludedCost < originalCost:
                res[0].append(i)
            else:
                if includedCost == originalCost:
                    res[1].append(i)    
        return res