class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 and edges == []:
            return [0]
        
        res = []
        minimumDepth = float('inf')
        
        adjacencyList = defaultdict(list)
        
        for i in edges:
            x, y = i
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        allLeafNodes = []
        
        for key, val in adjacencyList.items():
            if len(val) == 1:
                allLeafNodes.append(key)
                
        totalNodes = n
        # print(allLeafNodes)
        
        while totalNodes > 2:
            totalNodes -= len(allLeafNodes)
            nextLeafNodes = []
            
            for i in allLeafNodes:
                
                neighbourOfLeaf = adjacencyList[i].pop()
                adjacencyList[neighbourOfLeaf].remove(i)
                
                if len(adjacencyList[neighbourOfLeaf]) == 1:
                    nextLeafNodes.append(neighbourOfLeaf)
            allLeafNodes = nextLeafNodes
            
        return allLeafNodes