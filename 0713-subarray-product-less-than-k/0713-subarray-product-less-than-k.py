class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        count = 0
        left = 0
        right = 0
        currProd = 1
        while right < len(nums):
            currProd *= nums[right]
            while left < right and currProd >= k:
                currProd = currProd // nums[left]
                left+=1
            if currProd < k:
                count+=(right - left + 1)
            right+=1
        return count
