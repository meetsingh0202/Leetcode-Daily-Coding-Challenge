class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        occupied = set()
        
        adjacencyList = defaultdict(list)
        
        for i in pairs:
            x, y = i
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        sortedS = sorted(list(s))
        
        def traverse(currIndex):
            visited.add(currIndex)
            
            component[componentCount].append(currIndex)
            
            for k in adjacencyList[currIndex]:
                if k not in visited:
                    traverse(k)
            
        component = defaultdict(list)
        componentCount = 0
        visited = set()
        
        res = [' '] * len(s)
        
        for i in range(len(s)):
            if i not in visited:
                traverse(i)
                componentCount += 1
        
        # print(component)
        
        for key, val in component.items():
            currStr = []
            
            for k in val:
                currStr.append(s[k])
            
            currStr.sort()
            val.sort()
            
            for k in range(len(val)):
                res[val[k]] = currStr[k]
            
            # print(res)
            
        return "".join(res)