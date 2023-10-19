class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def traverse(currNode):
            
            if currNode not in visited:
                if currNode in HashMap:
                    self.maxLen = max(self.maxLen, len(stack) - HashMap[currNode])
                elif edges[currNode] != -1:
                    HashMap[currNode] = len(stack)
                    stack.append(currNode)
                    traverse(edges[currNode])
                    stack.pop()
                    HashMap.pop(currNode)
                visited.add(currNode)       

        self.maxLen = float('-inf')
        stack = []
        HashMap = dict()
        visited = set()
        
        for i in range(len(edges)):
            traverse(i)
        
        return self.maxLen if self.maxLen > 0 else -1