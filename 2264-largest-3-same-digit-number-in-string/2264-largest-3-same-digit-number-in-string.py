class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        for i in range(9, -1, -1):
            currStr = str(i) * 3
            
            if currStr in num:
                return currStr
        
        return ""