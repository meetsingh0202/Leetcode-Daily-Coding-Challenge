class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        if len(s1) > len(s2):
            return False
        
        HashMap1 = dict()
        
        for i in range(len(s1)):
            HashMap1[s1[i]] = 1 + HashMap1.get(s1[i], 0)            
            
        left = 0 
        Matched = 0
        
        for right in range(len(s2)):
            if s2[right] in HashMap1:
                HashMap1[s2[right]] -= 1
                if HashMap1[s2[right]] == 0:
                    Matched += 1
            
            if right >= len(s1) and s2[right - len(s1)] in HashMap1:
                if HashMap1[s2[right - len(s1)]] == 0:
                    Matched -= 1
                HashMap1[s2[right - len(s1)]] += 1
            
            if Matched == len(HashMap1):
                return True
        return False
