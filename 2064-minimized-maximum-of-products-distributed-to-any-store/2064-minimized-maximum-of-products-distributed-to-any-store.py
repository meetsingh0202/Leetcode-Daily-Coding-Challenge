class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def check(mid):
            currCount = 0
            
            for i in quantities:
                currCount += (i // mid)
                currCount += (1 if i % mid > 0 else 0)
            return currCount
        
        low = 1
        high = max(quantities)
        ans = 0
        
        while low <= high:
            
            mid = (low + high) >> 1
            
            if check(mid) <= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans