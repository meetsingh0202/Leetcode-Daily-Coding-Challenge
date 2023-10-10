class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        res = length

        right = 0

        for left in range(len(nums)):
            currElement = nums[left]

            while right < len(nums) and nums[right] < currElement + length:
                right += 1

            currWindowSize = right - left
            res = min(res, length - currWindowSize)

        return res