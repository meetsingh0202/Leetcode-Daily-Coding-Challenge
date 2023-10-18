class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        G = defaultdict(list)
        
        for v, w in prerequisites:
            G[v].append(w)
            
        def dfs(v, t, visited):
            if v in visited: 
                return False
            
            visited.add(v)
            
            if v == t:
                return True
            
            for w in G[v]:
                if dfs(w, t, visited):
                    return True
            
            return False
        
        res = []
        
        for v, w in queries:
            visited = set()
            res.append(dfs(v, w, visited))
        return res
            
class Solution1:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def check(a, b):
            
            flag = False
            
            for requirement in requirements[b]:
                if requirement == a:
                    flag = True
                    break
                flag = flag | check(a, requirement)
            
            return flag
            
        
        requirements = defaultdict(set)
        
        requiredBy = defaultdict(list)
        forwaredTo = defaultdict(list)
        
        for i in prerequisites:
            x, y = i
            
            requiredBy[y].append(x)
            forwaredTo[x].append(y)
        
        queue = deque([])
        
        for i in range(numCourses):
            if i not in requiredBy:
                queue.append(i)
                
        while queue:
            for i in range(len(queue)):
                currNode = queue.popleft()
                
                for k in forwaredTo[currNode]:
                    requiredBy[k].remove(currNode)
                    requirements[k].add(currNode)
                    
                    if len(requiredBy[k]) == 0:
                        del requiredBy[k]
                        queue.append(k)
        
        res = []
        
        for i in queries:
            x, y = i
            if check(x, y):
                res.append(True)
            else:
                res.append(False)
                
        return res
