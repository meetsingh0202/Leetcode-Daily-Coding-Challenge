class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] > nums[i]:
                new_bars = (nums[i-1] + nums[i] - 1) // nums[i]   # new_bars = ceil(nums[i-1]/nums[i])
                res += (new_bars - 1)   # cut = new_bars - 1
                nums[i-1] = nums[i-1] // new_bars   # max(nums[i-1]) = floor(nums[i-1]/new_bars)
            i -= 1
        return res