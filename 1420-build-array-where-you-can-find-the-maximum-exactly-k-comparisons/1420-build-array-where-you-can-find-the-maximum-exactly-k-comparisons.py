class Solution:
    def numOfArrays(self, n: int, m: int, K: int) -> int:
        if K > m: return 0

        MOD = int(1e9 + 7)

        @cache
        def rec(i, k, maxele):
            if k == 0:
                return pow(maxele, n - i, MOD)
            
            if k > n - i or k > m - maxele:
                return 0 
            
            count = 0
            for a in range(maxele + 1, m + 1):
                count = (count + rec(i + 1, k - 1, a)) % MOD
            
            count = (count + (maxele * rec(i + 1, k, maxele) ) % MOD) % MOD
            
            return count
    
        return rec(0, K, 0)