class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        HashMap = dict()
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        for key, value in HashMap.items():
            
            for k in range(value):
                if k >= len(res):
                    res.append([])
                    
                res[k].append(key)
        
        return res