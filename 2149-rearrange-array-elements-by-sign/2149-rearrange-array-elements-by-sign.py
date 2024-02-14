class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []
        
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
        i = 0
        j = 0
        res = []
        
        while len(res) < len(nums):
            
            if i < len(pos):
                res.append(pos[i])
                i += 1
            
            if j < len(neg):
                res.append(neg[j])
                j += 1
        
        return res
            
            