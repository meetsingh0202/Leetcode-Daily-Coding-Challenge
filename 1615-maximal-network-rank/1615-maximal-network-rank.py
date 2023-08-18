class Solution:
    def maximalNetworkRank(self, numCities: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(set) 

        for startCity, endCity in roads:

            adjList[startCity].add((startCity, endCity))  
            adjList[endCity].add((startCity, endCity))

        maxRank = 0

        for city1 in range(numCities-1):
            
            for city2 in range(city1+1, numCities):
                connections = adjList[city1].union(adjList[city2])

                rank = len(connections)

                maxRank = max(maxRank, rank)

        return maxRank