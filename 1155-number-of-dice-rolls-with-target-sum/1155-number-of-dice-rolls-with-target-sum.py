class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def traverse(currIndex, currTarget):
            if currIndex == n:
                return currTarget == target
            
            count = 0
            
            for i in range(1, k + 1):
                count += traverse(currIndex + 1, currTarget + i)
            
            return count % MOD
        
        MOD = (10**9 + 7)
        return traverse(0, 0) % MOD