class Solution:
    def calculateSum(self, nums, cost, target):
        result = 0
        for v, c in zip(nums, cost):
            result += abs(v - target) * c
        return result
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        s, f = min(nums), max(nums)
        
        while s < f:
            mid = (s + f) // 2
            left, right = self.calculateSum(nums, cost, mid), self.calculateSum(nums, cost, mid + 1)
            if left < right:
                f = mid
            else:
                s = mid + 1
        
        return self.calculateSum(nums, cost, s)
