class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        s1 = list(a)
        s2 = list(b)
        
        if len(s1) < len(s2):
            diff = len(s2) - len(s1)
            s1 = ['0'] * diff + s1
        else:
            diff = len(s1) - len(s2)
            s2 = ['0'] * diff + s2
            
        carry = 0
        ans = ""
        
        while s1 and s2:
            
            tempA = int(s1.pop())
            tempB = int(s2.pop())
            
            if tempA == 1 and tempB == 1:
                if carry:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                carry = 1

            elif tempA == 1 and tempB == 0:
                if carry:
                    ans = '0' + ans
                else:
                    ans = '1' + ans
                    carry = 0
                
            elif tempA == 0 and tempB == 1:
                if carry:
                    ans = '0' + ans
                else:
                    ans = '1' + ans
                    carry = 0
            else:
                if carry:
                    ans = '1' + ans
                    carry = 0
                else:
                    ans = '0' + ans
        if carry:
            ans = '1' + ans
            
        return ans
                
