class Solution1:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        prod = 1
        
        for i in range(n):
            if i % 2:
                prod = (prod * 4) % MOD
            else:
                prod = (prod * 5) % MOD
            
        return prod % MOD
    
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, y, p):
            res = 1
            x = x % p 
            if (x == 0):
                return 0
            while (y > 0):
                if ((y & 1) == 1):
                    res = (res * x) % p
                y = y >> 1
                x = (x * x) % p
            return res

        MOD = 1000000007
        oddPlaces = n // 2
        evenPlaces = n - oddPlaces
        
        prod = power(4, oddPlaces, MOD) * power(5, evenPlaces, MOD)
                
        return prod % MOD