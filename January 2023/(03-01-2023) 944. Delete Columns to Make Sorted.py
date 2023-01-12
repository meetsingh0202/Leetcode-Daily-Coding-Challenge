class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for s in zip(*strs):            
            for i in range(1,len(strs)):
                if ord(s[i]) < ord(s[i-1]):
                    count += 1
                    break
        return count
