class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = {}
        def rec_dp(n,k):
            if (n,k) in dp:
                return dp[(n,k)]
            
            if k < 0 or n <= 0:
                return 0
            if k == 0 and n > 0:
                return 1
            if n == 1 and k >= 1:
                return 0
            
            dp[(n,k)] = (rec_dp(n, k-1) + rec_dp(n-1,k) - rec_dp(n-1,k-n)) % 1000000007
            return dp[(n,k)]
        
        return rec_dp(n,k)