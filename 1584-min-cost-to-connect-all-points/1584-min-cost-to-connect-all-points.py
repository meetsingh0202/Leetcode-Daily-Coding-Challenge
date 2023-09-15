class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def calculateCost(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        
        heap = []
        visited = set()
        totalCost = 0
        
        visited = set()
        n = len(points)
        heap = [(0, 0)]
        
        while len(visited) < n: 
            currCost, currNode = heappop(heap)
            
            if currNode in visited:
                continue
                
            visited.add(currNode)
            totalCost += currCost
            
            for i in range(n):
                if i not in visited:
                    tempDist = calculateCost(points[i][0], points[i][1], points[currNode][0], points[currNode][1])
                    heappush(heap, [tempDist, i])
                    
        return totalCost
