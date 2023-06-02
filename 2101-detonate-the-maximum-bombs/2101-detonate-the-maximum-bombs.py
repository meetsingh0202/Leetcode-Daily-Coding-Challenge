class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def checkBoundary(x1, y1, r1, x2, y2):
            if radius1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
                return True
            return False
        
        adjacencyList = defaultdict(list)
        counter = 0
        
        for i in range(len(bombs)):
            x1, y1, radius1 = bombs[i]
            
            for j in range(len(bombs)):
                x2, y2, radius2 = bombs[j]
                
                if checkBoundary(x1, y1, radius1, x2, y2):
                    adjacencyList[i].append(j)
        
        
        def traverse(currNode):
            visited.add(currNode)
            currCount = 1
            
            for neigh in adjacencyList[currNode]:
                if neigh not in visited:
                    currCount += traverse(neigh)
            return currCount 
        
        maxBombs = 0
        
        for i in range(len(bombs)):
            visited = set()
            maxBombs = max(maxBombs, traverse(i))
        return maxBombs
                
            