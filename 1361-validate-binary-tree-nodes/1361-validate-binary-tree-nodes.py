class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        s = [0]
        visited = defaultdict(bool)
        
        for i in range(n):
            if leftChild[i] == s[0] or rightChild[i] == s[0]:
                s[0] = i
                       
        while s:
            node = s.pop(0)
                
            if visited[node]: 
                return False
            
            n -= 1
            visited[node] = True
            
            if leftChild[node] != -1:
                s.append(leftChild[node])
            if rightChild[node] != -1:
                s.append(rightChild[node])
        
        return n == 0
        
    def validateBinaryTreeNodes1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            HashSet = set()
            
            for i in leftChild:
                HashSet.add(i)
            
            for i in rightChild:
                HashSet.add(i)
            
            rootNodes = []
            
            for i in range(n):
                if i not in HashSet:
                    rootNodes.append(i)
            
            return rootNodes
        
        def findParent(currNode):
            visited.add(currNode)
            
            if currNode in left:
                parent[left[currNode]].append(currNode)
                if left[currNode] not in visited: 
                    findParent(left[currNode])
            
            if currNode in right:
                parent[right[currNode]].append(currNode)
                if right[currNode] not in visited:
                    findParent(right[currNode])
        
        parent = defaultdict(list)
        left = dict()
        right = dict()
        visited = set()
        
        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                left[i] = leftChild[i]
            
        for i in range(len(rightChild)):
            if rightChild[i] != -1:
                right[i] = rightChild[i]
            
        rootNodes = findRoot()
        
        if len(rootNodes) > 1 or len(rootNodes) == 0:
            return False
        
        findParent(rootNodes[0])
        rootNode = False
        
        for i in range(n):
            
            if i not in parent:
                if rootNode == False:
                    rootNode = True
                    continue
                else:
                    return False

            val = parent.get(i, [])
            
            if len(val) > 1:
                return False
            
        return True if rootNode else False