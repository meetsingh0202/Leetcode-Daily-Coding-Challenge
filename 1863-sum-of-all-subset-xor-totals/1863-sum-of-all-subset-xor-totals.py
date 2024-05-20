class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def calculate_xor(arr):
            res=arr[0]
            for i in arr[1:]:
                res=res^i
            return res
                
        def PowerSet(nums):
            n = len(nums)
            output = []
            for i in range(2**n, 2**(n + 1)):
                bitmask = bin(i)[3:]
                output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            return output
                    
        
        allsubsets=PowerSet(nums)
        result=0
        # print(allsubsets)
        for i in allsubsets:
            if i!=[]:
                result=result+calculate_xor(i)
        return result
            
        