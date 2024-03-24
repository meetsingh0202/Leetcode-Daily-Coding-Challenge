class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in nums:
            temp = abs(i)
            if nums[temp] < 0:
                return temp
            nums[temp] *= -1