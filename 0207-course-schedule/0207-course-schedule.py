class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacencyList = defaultdict(list)
        dependent = set()
        visited = set()
        needCourses = defaultdict(set)
        gotCourses = defaultdict(set)
        
        for i in prerequisites:
            x, y = i
            adjacencyList[x].append(y)
            needCourses[y].add(x)
            dependent.add(y)
            
        q = deque([])
        count = 0
            
        for i in range(numCourses):
            if i not in dependent:
                q.append(i)
                count += 1
                
        while q:
            currCourse = q.popleft()
            for i in adjacencyList[currCourse]:
                gotCourses[i].add(currCourse)
                if len(gotCourses[i]) == len(needCourses[i]):
                    q.append(i)
                    count += 1
                    
        return count == numCourses