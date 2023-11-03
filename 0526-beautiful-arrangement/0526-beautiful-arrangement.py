class Solution:
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