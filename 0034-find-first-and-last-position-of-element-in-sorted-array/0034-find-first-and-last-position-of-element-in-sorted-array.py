class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums):
            low = 0
            high = len(nums) - 1
            ans = 0
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        
        def findLast(nums):
            low = 0
            high = len(nums) - 1
            ans = 0
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        a = findFirst(nums)
        b = findLast(nums)
        if (a != 0 and b != 0) or (nums and nums[0] == target):
            return [a, b]
        return [-1, -1]