class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        l = []
        res = 0
        
        for i in s:
            temp = (ord(i) - 96)
            for i in str(temp):
                l.append(int(i))
            
        while k:
            currSum = sum(l)
            res = currSum
            l = []
            for i in str(currSum):
                l.append(int(i))
            k -= 1
            
        return res
