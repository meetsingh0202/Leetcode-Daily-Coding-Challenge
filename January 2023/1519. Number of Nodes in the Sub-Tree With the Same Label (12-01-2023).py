class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        AdjacencyList = defaultdict(list)
        for i in edges:
            a, b = i
            AdjacencyList[a].append(b)
            AdjacencyList[b].append(a)
        
        def traverse(root):
            def MergeDict(temp, dict1):
                for key, val in dict1.items():
                    temp[key] = val + temp.get(key, 0)
                return temp
            
            if root == None:
                return {}
            
            temp = {}
            visited.add(root)
            for i in AdjacencyList[root]:
                if i not in visited:
                    temp = MergeDict(temp, traverse(i))
                
            currChar = labels[root]
            temp[currChar] = 1 + temp.get(currChar, 0)
            res.append((root, temp[labels[root]]))
            return temp
            
        res = []
        visited = set()
        traverse(0)
        res.sort()
        ans = [0] * len(labels)
        
        for a, b in res:
            ans[a] = b
        return ans
