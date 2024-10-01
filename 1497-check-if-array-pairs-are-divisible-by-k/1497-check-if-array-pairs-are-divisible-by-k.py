class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        
        for num in arr:
            rem = (num % k + k) % k
            remainder_count[rem] += 1
        
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return remainder_count[0] % 2 == 0
