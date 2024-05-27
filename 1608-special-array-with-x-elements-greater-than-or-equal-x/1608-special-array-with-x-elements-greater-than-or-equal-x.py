class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= nums[0]:
            return len(nums)
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            x = len(nums) - mid
        
            if nums[mid] >= x:
                if nums[mid-1] < x:
                    return x
                right = right - 1
            else:
                left = left + 1
        
        return -1