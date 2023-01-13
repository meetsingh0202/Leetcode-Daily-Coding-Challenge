class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        AdjacencyList = defaultdict(list)
        for index in range(len(parent)):
            AdjacencyList[parent[index]].append(index)
            
        def traverse(root):
            nonlocal Max
            
            temp = 1
            for i in AdjacencyList[root]:
                nextLength = traverse(i)
            
                if s[root] != s[i]:
                    Max = max(Max, temp + nextLength)
                    temp = max(temp, nextLength + 1)
            
            return temp
        
        Max = 1
        traverse(0)
        return Max                
            
            
