class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def traverse(currNode):
            if currNode in visited:
                return False
            
            if currNode == destination:
                return True
            
            visited.add(currNode)
            
            res = False
            for neighbour in adjacencyList[currNode]:
                res = res | traverse(neighbour)
            
            return res
        
        adjacencyList = defaultdict(list)
        
        visited = set()
        
        for i in edges:
            x, y = i
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        return traverse(source)