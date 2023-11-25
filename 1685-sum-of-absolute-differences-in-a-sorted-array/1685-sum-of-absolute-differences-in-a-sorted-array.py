class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        totalSum = sum(nums)
        
        res = []
        rightSum = 0
        leftSum = 0
        
        for i in range(len(nums)):
            if i != 0:
                rightSum = totalSum - leftSum - nums[i]
                rightLen = len(nums) - i - 1
                leftLen = i
                currSum = leftLen * nums[i] - leftSum
                currSum += (rightSum - rightLen * nums[i])
                # print(leftSum, rightSum, leftLen * nums[i] - leftSum, rightSum - rightLen * nums[i])
                leftSum += nums[i]
                res.append(abs(currSum))
            else:
                res.append(totalSum - len(nums) * nums[i])
                leftSum += nums[i]
        return res