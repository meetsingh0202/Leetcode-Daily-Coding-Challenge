class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        minElement = min(nums)
        
        arr = list(set(nums))
        arr.sort()
        
        HashMap = dict()
        count = 0
        
        for i in range(len(arr)):
            HashMap[arr[i]] = i
        
        # print(HashMap)
        
        for i in nums:
            count += HashMap[i]
            
        return count