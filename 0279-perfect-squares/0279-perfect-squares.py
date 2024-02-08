class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                sqaure = j * j
                dp[i] = min(dp[i], 1 + dp[i - sqaure])
                
        return dp[n]