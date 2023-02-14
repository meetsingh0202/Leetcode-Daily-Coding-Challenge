class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index,currSequence):
            if index==len(nums):
                if len(currSequence)>1:                
                    res.add(tuple(currSequence))
                return
            
            if len(currSequence)>=2:
                res.add(tuple(currSequence))
            
            prevElement=currSequence[-1] if len(currSequence)>0 else -101
            
            currElement=nums[index]
            
            if prevElement<=currElement:
                backtrack(index+1,currSequence+[currElement])
                
            backtrack(index+1,currSequence)
            
        res=set()
        backtrack(0,[])
        return res
