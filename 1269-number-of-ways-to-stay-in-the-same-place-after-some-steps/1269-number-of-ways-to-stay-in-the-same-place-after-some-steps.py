class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def traverse(currSteps, currIndex):
            if currSteps == 0:
                return 1 if currIndex == 0 else 0 
            
            right, left, stay = 0, 0, 0
            
            if currIndex - 1 >= 0:
                left = traverse(currSteps - 1, currIndex - 1)
            
            if currIndex + 1 < arrLen:
                right = traverse(currSteps - 1, currIndex + 1)
                
            stay = traverse(currSteps - 1, currIndex)
            
            return (right + left + stay) % MOD
        
        MOD = 1000000007
        return traverse(steps, 0) % MOD