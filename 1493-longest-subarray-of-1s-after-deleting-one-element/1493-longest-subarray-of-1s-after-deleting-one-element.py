class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        HashMap = dict()
        left = 0
        Max = 0
        
        for right in range(len(nums)):
            currVal = nums[right]
            
            HashMap[currVal] = 1 + HashMap.get(currVal, 0)
            
            while HashMap.get(0, 0) > 1:
                HashMap[nums[left]] -= 1
                left += 1
            
            Max = max(Max, right - left)
        
        return Max