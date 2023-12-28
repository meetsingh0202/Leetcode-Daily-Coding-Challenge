class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache
        def traverse(index, prev, currCount, currK):
            if currK < 0:
                return float('inf')
            
            if index >= len(s):
                return 0
            
            delete = traverse(index + 1, prev, currCount, currK - 1)
            keep = 0
            if s[index] == prev:
                if currCount == 1 or currCount == 9 or currCount == 99:
                    keep += 1
                keep += traverse(index + 1, prev, currCount + 1, currK)
            else:
                keep = 1 + traverse(index + 1, s[index], 1, currK)
            
            return min(delete, keep)
        
        return traverse(0, 0, 0, k)
        