class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacencyList = defaultdict(list)

        for source, destination, cost in flights:
            adjacencyList[source].append([destination, cost])
            
        visited = set()
        queue = [(0, k, src)]
        
        while queue:
            currCost, currSteps, lastNode = heapq.heappop(queue)
            
            if lastNode == dst:
                return currCost
            
            if currSteps >= 0:
                for nextNode, cost in adjacencyList[lastNode]:
                    if (currCost , nextNode) not in visited:
                        visited.add((currCost, nextNode))
                        nextComputation = (currCost + cost, currSteps - 1, nextNode)
                        heapq.heappush(queue, nextComputation)
        return -1
