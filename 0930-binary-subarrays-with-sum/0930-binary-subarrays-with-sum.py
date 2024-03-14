class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict1={0:1}
        prefixsum=0   
        total=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            if prefixsum-goal in dict1:
                total+=dict1[prefixsum-goal]
            if prefixsum in dict1:
                dict1[prefixsum]+=1
            else:
                dict1[prefixsum]=1
        return total