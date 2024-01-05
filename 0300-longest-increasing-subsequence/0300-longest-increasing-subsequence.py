class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        Max=0
        for i in range(n):
            Max=0
            for j in range(i):
                if nums[i] > nums[j]:
                    Max=max(Max,dp[j])
            dp[i] = Max+1
                    
        return max(dp)