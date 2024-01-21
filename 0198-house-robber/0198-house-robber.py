class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for index in range(1, len(nums)):
            notTake = float('-inf')
            Take = float('-inf')
            
            notTake = dp[index - 1]
            Take = nums[index] + (dp[index - 2] if index - 2 >= 0 else 0)
            dp[index] = max(notTake, Take)
        return dp[-1]