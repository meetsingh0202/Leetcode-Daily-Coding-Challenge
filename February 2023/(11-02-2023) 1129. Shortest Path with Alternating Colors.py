class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjacencyListRED = defaultdict(list)
        adjacencyListBLUE = defaultdict(list)
        
        for i in redEdges:
            x, y = i
            adjacencyListRED[x].append(y)
            
        for i in blueEdges:
            x, y = i
            adjacencyListBLUE[x].append(y)
        
        res = [float('inf')] * n
        res[0] = 0
        
        for i in range(1, n):
            destination = i
            q = deque([[0, 'R', -1, 0, set()], [0, 'B', -1, 0, set()]])

            while q:
                currNode, lastColor, lastNode, distance, visited = q.popleft()
                if distance >= res[destination]:
                    continue
                    
                if currNode == destination:
                    res[destination] = min(res[destination], distance)
                    continue

                visited.add((currNode, lastColor))

                if lastColor == 'R':
                    for i in adjacencyListBLUE[currNode]:
                        if (i, 'B') not in visited:
                            q.append((i, 'B', currNode, distance + 1, visited))
                else:
                    for i in adjacencyListRED[currNode]:
                        if (i, 'R') not in visited:
                            q.append((i, 'R', currNode, distance + 1, visited))
            
            if res[destination] == float('inf'):
                res[destination] = -1
            
        return res
