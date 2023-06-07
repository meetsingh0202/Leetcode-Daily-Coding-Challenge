class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count = 0
        
        while a or b or c:
            
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1
            
            if cBit == 1:
                if aBit or bBit:
                    pass
                else:
                    count += 1
            else:
                if aBit == 0 and bBit == 0:
                    pass
                elif aBit == 1 and bBit == 1:
                    count += 2
                elif aBit == 1 or bBit == 1:
                    count += 1
        
            a >>= 1
            b >>= 1
            c >>= 1
            
        return count