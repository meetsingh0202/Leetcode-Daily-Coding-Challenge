class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        def evaluateDecimal(HashMap):
            temp = 0
            for i in range(32):
                if HashMap[i]:
                    temp += (1 << i)
            return temp
        
        def removeElement(HashMap, num):
            for i in range(32):
                if num & (1 << i):
                    HashMap[i] -= 1
            return HashMap
        
        res = float('inf')
        
        HashMap = [0] * 32
        
        left = 0 
        
        for right in range(len(nums)):
            
            for i in range(32):
                if nums[right] & (1 << i):
                    HashMap[i] += 1
                    
            currOr = evaluateDecimal(HashMap)
            
            
            while currOr >= k and left <= right:
                res = min(res, right - left + 1)
                HashMap = removeElement(HashMap, nums[left])
                left += 1
                currOr = evaluateDecimal(HashMap)
            
        return res if res != float('inf') else -1