class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        sumTillNow = nums[0] + nums[1]
        
        for i in range(2, len(nums)):
            currVal = nums[i]
            if sumTillNow > currVal:
                ans = max(ans, sumTillNow + currVal)
            sumTillNow += currVal
        
        return ans