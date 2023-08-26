class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        res=[pairs[0]]
        for i in pairs[1:]:
            if res[-1][1]<i[0]:
                res.append(i)
        
        return len(res)