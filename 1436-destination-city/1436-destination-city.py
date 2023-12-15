class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        adjacencyList = defaultdict(list)
        
        for i in paths:
            x, y = i
            adjacencyList[x].append(y)
            
        for i in paths:
            x, y = i
            
            if y not in adjacencyList:
                return y