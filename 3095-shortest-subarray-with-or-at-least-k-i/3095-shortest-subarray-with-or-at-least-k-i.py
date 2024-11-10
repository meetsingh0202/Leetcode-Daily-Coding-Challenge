class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        res = float('inf')
        
        for i in range(len(nums)):
            curr = 0
            count = 0
            
            for j in range(i, len(nums)):
                curr |= nums[j]
                count += 1
                
                if curr >= k and count < res:
                    res = count
        
        return res if res != float('inf') else -1