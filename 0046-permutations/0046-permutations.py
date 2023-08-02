class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traverse(tempnums,currPath):
            if len(currPath)==len(nums):
                res.append(currPath)
                return 
            visited=set()
            for i in range(len(tempnums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    traverse(tempnums[:i]+tempnums[i+1:],currPath+[tempnums[i]])
        
        res=[]
        traverse(nums,[])
        return res