class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        HashSet = dict()
        
        for i in range(len(nums)):
            
            if (target - nums[i]) in HashSet:
                return [i, HashSet[(target - nums[i])]]
            
            HashSet[nums[i]] = i