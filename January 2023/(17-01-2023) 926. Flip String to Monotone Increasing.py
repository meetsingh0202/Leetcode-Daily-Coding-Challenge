class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def findLastIndex(s):
            l = -1
            for i in range(len(s)):
                if s[i] == '0':
                    l = i
            return l
        
        @cache
        def traverse(currIndex, lastChar):
            if currIndex == len(s):
                return 0
            
            change = float('inf')
            notChange = float('inf')
            
            if s[currIndex] == lastChar:
                notChange = traverse(currIndex + 1, s[currIndex])
            else:
                if lastChar == '1':
                    change = 1 + traverse(currIndex + 1, '1')
                else:
                    change1 = traverse(currIndex + 1, s[currIndex])
                    change2 = 1 + traverse(currIndex + 1, '0')
                    change = min(change1, change2)
                    
            return min(change, notChange)
        
        lastIndex = findLastIndex(s)
        return traverse(0, '0')
