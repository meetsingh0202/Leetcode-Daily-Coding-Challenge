from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        leftMin = nums[0]
        rightSl = SortedList(nums[2:])
        
        for i in range(1, len(nums)-1):
            cur = nums[i]
            if cur > leftMin:
                rightEl = rightSl.bisect_right(leftMin)
                if rightEl < len(rightSl) and rightSl[rightEl] < cur:
                    return True
            
            leftMin = min(leftMin, nums[i])
            rightSl.remove(nums[i+1])
        return False