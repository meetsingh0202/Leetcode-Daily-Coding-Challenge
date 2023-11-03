class Solution1:
    def countArrangement(self, n: int) -> int:
        
        
        def traverse(currIndex):
            if currIndex > n:
                self.count += 1
                return
            
            for i in range(1, n + 1):
                if i not in visited:
                    if i % currIndex == 0 or currIndex % i == 0:
                        visited.add(i)
                        traverse(currIndex + 1)
                        visited.remove(i)
        
        self.count = 0
        visited = set()
        traverse(1)
        return self.count
    
class Solution:
    def countArrangement(self, n: int) -> int:
        
        def getKthBit(n, k):
            return ((n >> k) % 2)
        
        def setKthBit(n, k):
            return ((1 << k) | n)
        
        @cache
        def traverse(currIndex, visited):
            if currIndex > n:
                return 1
            
            count = 0
            
            for i in range(1, n + 1):
                if getKthBit(visited, i) == False:
                    if currIndex % i == 0 or i % currIndex == 0:
                        count += traverse(currIndex + 1, setKthBit(visited, i))
                    
            return count
        
        return traverse(1, 0)