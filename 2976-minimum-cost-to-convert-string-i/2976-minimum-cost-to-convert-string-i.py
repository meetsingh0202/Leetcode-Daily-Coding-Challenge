class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
#         def traverse(currNode, target):
#             if (currNode, target) in minCost:
#                 return minCost[(currNode, target)]
            
#             if currNode == target:
#                 return 0
            
#             minimumCost = float('inf')
            
#             for neigh, neighCost in adjacencyList[currNode]:
#                 if neigh not in visited:
#                     visited.add(neigh)
#                     minimumCost = min(minimumCost, neighCost + traverse(neigh, target))
#                     visited.remove(neigh)
                    
#             return minimumCost
        
        minCost = [[float('inf')] * 26 for i in range(26)]
        adjacencyList = [[float('inf')] * 26 for i in range(26)]
        
        for i in range(len(original)):
            src, dest, currCost = original[i], changed[i], cost[i]
            if src == dest:
                continue
            adjacencyList[ord(src) - 97][ord(dest) - 97] = min(adjacencyList[ord(src) - 97][ord(dest) - 97], currCost)
        
        for i in range(97, 97 + 26):
            currChar = chr(i)
            minCost[i - 97][i - 97] = 0           
            
            start_vertex = i - 97
            minCost[start_vertex][start_vertex] = 0
            visited = [False] * 26

            for _ in range(26):
                min_distance = float('inf')
                u = None
                for j in range(26):
                    if not visited[j] and minCost[start_vertex][j] < min_distance:
                        min_distance = minCost[start_vertex][j]
                        u = j

                if u is None:
                    break

                visited[u] = True

                for v in range(26):
                    if adjacencyList[u][v] != 0 and not visited[v]:
                        alt = minCost[start_vertex][u] + adjacencyList[u][v]
                        if alt < minCost[start_vertex][v]:
                            minCost[start_vertex][v] = alt
                            
        totalCost = 0
        
        for i in range(len(source)):
            currChar = source[i]
            targetChar = target[i]
            
            if currChar != targetChar:
                if minCost[ord(currChar) - 97][ord(targetChar) - 97]!= float('inf'):
                    totalCost += minCost[ord(currChar) - 97][ord(targetChar) - 97]
                else:
                    return -1
                
        return totalCost if totalCost != float('inf') else -1
