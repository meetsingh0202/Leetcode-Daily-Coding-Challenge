class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix = [nums[0]]
        res = []

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        for i in range(len(nums)):
            currVal = nums[i]
            currIndex = i

            if currIndex - k < 0:
                res.append(-1)
            elif currIndex + k >= len(nums):
                res.append(-1)
            else:
                leftSum = prefix[currIndex] - (prefix[currIndex - k - 1] if currIndex - k - 1 >= 0 else 0)
                rightSum = prefix[currIndex + k] - prefix[currIndex]
                res.append((leftSum + rightSum) // (2 * k + 1))
        
        return res