class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, target):
            if i == len(nums):
                return 1 if target == 0 else 0
            return dfs(i + 1, target + nums[i]) + dfs(i+1, target - nums[i])
        
        return dfs(0, target)