class Solution:    
    def uniquePaths(self, m: int, n: int) -> int:
        
        ways = m + n - 2
        r = max(m - 1, n - 1) # or n - 1
        res = 1
        for i in range(1, r + 1):
            res = res * (ways - r + i) // i
        return int(res)