class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        target = totalSum // 2
        
        if totalSum % 2 == 1:
            return False
        
        @cache
        def traverse(currIndex, currSum1, currSum2):
            if currIndex == len(nums):
                return currSum1 == target and currSum2 == target
            
            if currSum1 > target or currSum2 > target:
                return False
            
            includeInOne = traverse(currIndex + 1, currSum1 + nums[currIndex], currSum2)
            includeInTwo = traverse(currIndex + 1, currSum1, currSum2 + nums[currIndex])
            
            return includeInOne or includeInTwo
            
        memo = dict()
        return traverse(0, 0, 0)