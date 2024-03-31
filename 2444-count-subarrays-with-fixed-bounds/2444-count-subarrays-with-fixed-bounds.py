class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        start = -1
        
        prevMin = -1
        prevMax = -1
        
        for index, val in enumerate(nums):
            if val == minK:
                prevMin = index
            if val == maxK:
                prevMax = index
            if val < minK or val > maxK:
                start = index
            res += (max(0, min(prevMin, prevMax) - start))
        return res
        