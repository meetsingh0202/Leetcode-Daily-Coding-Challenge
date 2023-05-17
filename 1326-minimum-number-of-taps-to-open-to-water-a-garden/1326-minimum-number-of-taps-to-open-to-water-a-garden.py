class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [(n + 3)] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            currVal = ranges[i]
            leftRange = max(0, i - currVal)
            rightRange = min(n, i + currVal)
            
            for j in range(leftRange, rightRange + 1):
                dp[j] = min(dp[j], dp[leftRange] + 1)

        if dp[n] != n + 3:
            return dp[n]
        return -1