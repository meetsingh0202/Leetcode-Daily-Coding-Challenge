class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def traverse(currNode, lastNode):
            count[currNode] = 0
            visited.add(currNode)
            
            for i in graph[currNode]:
                if i not in visited:
                    if traverse(i, currNode):
                        pass
                    else:
                        count[currNode] += 1
                        break
                else:
                    if isSafe[i] == True:
                        continue
                    count[currNode] += 1
                    break
                        
            flag = True if count[currNode] == 0 else False
            isSafe[currNode] = flag
            
            
            return isSafe[currNode]
        
        visited = set()
        isSafe = [False] * len(graph)
        count = [0] * len(graph)
        res = []
        
        for i in range(len(graph)):
            if i not in visited:
                traverse(i, -1)
        
        for i in range(len(graph)):
            if isSafe[i]:
                res.append(i)
        
        return res