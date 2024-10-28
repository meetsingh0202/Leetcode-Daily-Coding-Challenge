class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        HashMap = dict()
        count = [0 for i in range(26)]
        MOD = 10**9 + 7
        
        for i in s:
            currElement = ord(i) - 97
            count[currElement] += 1
            
        for i in range(t):
            
            temp = [0 for i in range(26)]
            
            for i in range(26):
                if  i == 25:
                    temp[0] += count[25]
                    temp[1] += count[25] 
                    
                else:
                    temp[i + 1] += count[i] 
            
            count = temp
        
        return sum(count) % MOD
        
