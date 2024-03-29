class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        adjacencyList = defaultdict(list)
        
        # isReachable = [[False for i in range(numCourses)] for j in range(numCourses)]
        isReachable = defaultdict(set)
        
        
        for i in prerequisites:
            x, y = i
            adjacencyList[x].append(y)
        
        for i in range(numCourses):
            
            queue = deque([])
            queue.append(i) 
            visited = set()
            
            while queue:
                for _ in range(len(queue)):
                    currNode = queue.popleft()
                    visited.add(currNode)
                    
                    isReachable[i].add(currNode)
                    
                    for k in adjacencyList[currNode]:
                        if k not in visited:
                            queue.append(k)
        
        res = []
        for x, y in queries:
            if y in isReachable[x]:
                res.append(True)
            else:
                res.append(False)
            # res.append(isReachable[x][y])
        return res