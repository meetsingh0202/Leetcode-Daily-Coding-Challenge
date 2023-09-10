class Solution:
    def countOrders(self, n: int) -> int:
        
        cache = dict()

        def dp(picked, delivered):
            if (picked, delivered) in cache:
                return cache[(picked, delivered)]
            if picked == delivered == n:
                return 1
            if picked > n or delivered > n: 
                return 0
            if delivered > picked:
                return 0
            
            res = 0
            res += (n - picked) * dp(picked + 1, delivered)
            res += (picked - delivered) * dp(picked, delivered + 1)
            cache[(picked, delivered)] = res
            return res
        
        return dp(0, 0) % (10**9 + 7)