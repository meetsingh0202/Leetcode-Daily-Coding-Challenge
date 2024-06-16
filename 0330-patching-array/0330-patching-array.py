class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        currSum = 1
        patch = 0
        i = 0
        while currSum <= n:
            if i < len(nums) and nums[i]<=currSum:
                currSum += nums[i]
                i += 1
            else:
                currSum += currSum
                patch += 1
        return patch
