class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    
        def countPairs(nums, target):
            count = 0
            left, right = 0, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    count += right - left
                    left += 1

            return count

        nums.sort()
        return countPairs(nums, upper) - countPairs(nums, lower - 1)