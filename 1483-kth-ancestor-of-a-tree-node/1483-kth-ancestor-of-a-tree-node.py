class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = 0
        while (1 << self.log) <= n:
            self.log += 1

        self.ancestor = [[-1 for i in range(self.log)] for j in range(n)]
        self.depth = [0 for i in range(n)]
        
        child = defaultdict(list)
        
        for index in range(1, len(parent)):
            child[parent[index]].append(index)
        
        def findDepth(node, currDepth):
            self.depth[node] = currDepth
            
            for childNode in child[node]:
                findDepth(childNode, currDepth + 1)
            
        findDepth(0, 0)
    
        for j in range(self.log):
            for i in range(1, n):
                self.ancestor[i][0] = parent[i]

                if j > 0:
                    self.ancestor[i][j] = self.ancestor[ self.ancestor[i][j - 1] ][j - 1]
                
                # print(i, 2**j, self.ancestor[i][j])
        
    def getKthAncestor(self, node: int, k: int) -> int:
        # print("NODE: ", node, "K : ", k)
        
        if self.depth[node] < k:
            return -1
        
        for j in range(self.log):
            if (k & (1 << j)):
                node = self.ancestor[node][j]
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)