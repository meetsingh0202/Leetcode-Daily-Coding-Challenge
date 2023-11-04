class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors = []
        
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        
        return factors[k - 1] if len(factors) >= k else -1