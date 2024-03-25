class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index + 1)
            
            nums[index] = - nums[index]
        print(nums)
        return output
