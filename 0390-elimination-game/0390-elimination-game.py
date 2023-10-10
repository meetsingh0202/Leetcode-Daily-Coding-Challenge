class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1 
        step  = 1 
        flag = True
        
        while (n > 1):
            
            if flag or n % 2 != 0:
                head += step
                
            step *= 2 
            n //= 2
            flag = not flag

        return head