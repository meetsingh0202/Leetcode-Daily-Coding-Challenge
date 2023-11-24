class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        heap1 = []
        heap2 = []
        
        for i in range(len(piles)):
            index, val = i, piles[i]
            heappush(heap1, [-val, index])
            heappush(heap2, [val, index])
            
        visited = set()
        ans = 0
        count = 0
        totalCount = len(piles) // 3
        
        while count < totalCount:
            
            a, b, c = -1, -1, -1
            
            while heap1:
                val, index = heappop(heap1)
                
                if index in visited:
                    continue
                    
                val = val * -1
                visited.add(index)
                
                if a == -1:
                    a = val
                    
                elif b == -1:
                    b = val
                    break
                
            while heap2:
                val, index = heappop(heap2)
                
                if index in visited:
                    continue
                    
                c = val
                visited.add(index)
                break
            
            if a == -1 or b == -1 or c == -1:
                break
            
            ans += b
            count += 1
            
        return ans