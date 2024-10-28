class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums = set(nums)
        ans = -1

        for i in nums:
            c = 0
            x = i
            while x**2 in nums:
                c+=1
                x=x**2
        
            ans = max(ans,c)

        ans = ans + 1 if ans != 0 else -1
        return ans
