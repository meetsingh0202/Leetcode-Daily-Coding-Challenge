class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def traverse(currIndex, currMax, currD):
            if currIndex == len(jobDifficulty):
                if currD == 0:
                    return currMax
                return float('inf')
            
            if currD < 0:
                return float('inf')
            
            includeInCurrDay = traverse(currIndex + 1, max(currMax, jobDifficulty[currIndex]), currD)
            
            includeInNewDay = currMax + traverse(currIndex + 1, jobDifficulty[currIndex], currD - 1)
            
            return min(includeInCurrDay, includeInNewDay)
        
        ans = traverse(0, 0, d)
        
        if ans == float('inf'):
            return -1
        
        return ans