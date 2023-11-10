class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        def traverse(currNode):
            visited.add(currNode)
            
            res.append(currNode)
            
            for i in adjacencyList[currNode]:
                if i not in visited:
                    traverse(i)
        
        start = -1
        adjacencyList = defaultdict(list)
        
        for i in adjacentPairs:
            x, y = i
            
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        for k in adjacencyList:
            if len(adjacencyList[k]) == 1:
                start = k
        
        res = []
        visited = set()
        traverse(start)
        return res