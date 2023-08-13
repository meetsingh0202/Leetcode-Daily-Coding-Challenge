class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @cache
        def solve(index):
            if index == n:
                return True
            if index + 1 == n:
                return False
            if index + 2 == n:
                return nums[index] == nums[index+1]
            if index + 3 == n:
                return ((nums[index] == nums[index+1] and nums[index+1] == nums[index+2]) or (nums[index] + 1 == nums[index+1] and nums[index+1] + 1 == nums[index+2] ) )
            ans = False
            if nums[index] == nums[index+1]:
                ans = ans or solve(index+2)
            if ((nums[index] == nums[index+1] and nums[index+1] == nums[index+2]) or (nums[index] + 1 == nums[index+1] and nums[index+1] + 1 == nums[index+2] ) ):
                ans = ans or solve(index+3)
            return ans
        return solve(0)