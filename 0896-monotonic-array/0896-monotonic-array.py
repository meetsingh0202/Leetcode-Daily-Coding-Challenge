class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        DSorted = sorted(nums, reverse = True)
        ASorted = sorted(nums)
        
        if nums == DSorted or nums == ASorted:
            return True
        return False