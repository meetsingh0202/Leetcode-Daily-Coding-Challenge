class Solution:
    def longestPalindrome(self, s: str) -> str:    
        
        resL, resR = 0, 0
        resLen = 0
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r + 1
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1   
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r + 1
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return s[resL:resR]