class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        HashMap = dict()
        score = 0
        res = 0
        HashMap[0] = -1
        
        for index, val in enumerate(nums):
            if val == 0:
                score -= 1
            else:
                score += 1
            
            if score in HashMap:
                res = max(res, index - HashMap.get(score))
            else:
                HashMap[score] = index
        
        return res