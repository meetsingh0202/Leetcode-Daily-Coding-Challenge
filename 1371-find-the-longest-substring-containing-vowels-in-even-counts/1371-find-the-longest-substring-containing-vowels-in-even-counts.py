class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        HashMap = dict()
        HashMap['a'] = 1
        HashMap['e'] = 2
        HashMap['i'] = 4
        HashMap['o'] = 8
        HashMap['u'] = 16
        
        mask = 0
        maxLen = 0
        
        last = dict()
        last[0] = -1
        
        for i in range(len(s)):
            
            currChar = s[i]
            
            if currChar in HashMap:
                mask = mask ^ HashMap[currChar]
                
            if mask in last:
                maxLen = max(maxLen, i - last[mask])
            else:
                last[mask] = i
            
        return maxLen