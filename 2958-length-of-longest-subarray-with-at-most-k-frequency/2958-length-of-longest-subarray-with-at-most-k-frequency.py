class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        HashMap = dict()
        res = 0
        left = 0
        
        for right in range(len(nums)):
            
            HashMap[nums[right]] = 1 + HashMap.get(nums[right], 0)
            
            while HashMap[nums[right]] > k:
                
                HashMap[nums[left]] -= 1
                left += 1
                
            res = max(res, right - left + 1)
        
        return res