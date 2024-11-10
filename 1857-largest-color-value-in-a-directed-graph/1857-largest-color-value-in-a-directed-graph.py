class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        adjacencyList = defaultdict(list)
        
        for i in edges:
            x, y = i
            adjacencyList[x].append(y)
            
        def traverse(currIndex):
            
            if currIndex in path:
                return float('inf')
            
            if currIndex in visited:
                return 0
            
            visited.add(currIndex)
            path.add(currIndex)
            
            currColor = ord(colors[currIndex]) - ord('a')
            nodeScores[currIndex][currColor] = 1
            
            for neighbour in adjacencyList[currIndex]:
                
                if traverse(neighbour) == float('inf'):
                    return float('inf')
                
                for j in range(26):
                    nodeScores[currIndex][j] = max(nodeScores[currIndex][j], nodeScores[neighbour][j] + (1 if j == currColor else 0))
            
            path.remove(currIndex)
            return max(nodeScores[currIndex])
            
        visited, path = set(), set()
        nodeScores = [[0 for i in range(26)] for i in range(len(colors))]
        res = 0
        
        for i in range(len(colors)):
            res = max(res, traverse(i))
        
        return res if res != float('inf') else -1
                