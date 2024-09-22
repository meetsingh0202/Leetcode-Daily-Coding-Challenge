class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1
        
        while k > 0:
            count = 0
            first = current
            last = current + 1
            
            while first <= n:
                count += min(n + 1, last) - first
                first *= 10
                last *= 10
            
            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1
        
        return current
