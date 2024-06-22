class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        subarrayCount = 0
        res = 0
        oddCount = 0
        
        for right in range(len(nums)):
            
            if nums[right] & 1 == 1:
                oddCount += 1
                subarrayCount = 0
            
            while oddCount == k:
                if nums[left] & 1:
                    oddCount -= 1
                subarrayCount += 1
                left += 1
            
            res += subarrayCount
        
        return res