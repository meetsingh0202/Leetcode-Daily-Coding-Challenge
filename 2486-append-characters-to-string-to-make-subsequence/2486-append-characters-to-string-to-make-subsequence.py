class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        index1, index2 = 0, 0
        
        while index1 < len(s) and index2 < len(t):
            
            if s[index1] == t[index2]:
                index1 += 1
                index2 += 1
            
            else:
                index1 += 1
        
        return len(t) - index2
            