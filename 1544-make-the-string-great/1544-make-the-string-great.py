class Solution:
    def makeGood(self, s: str) -> str:
        
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1].lower() and s[i] > s[i + 1]:
                s = s[:i] + s[i + 2 :]
                i = 0
            elif s[i] == s[i + 1].upper() and s[i] < s[i + 1]:
                s = s[:i] + s[i + 2 :]
                i = 0
            else:
                i += 1
        return s
            