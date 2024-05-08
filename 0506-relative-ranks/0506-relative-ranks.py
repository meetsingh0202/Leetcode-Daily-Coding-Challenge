class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        score_sorted = sorted(score, reverse = True)
        d = {}
        
        for i in range(0, len(score)):
            if  i == 0:
                d[score_sorted[i]] = "Gold Medal"
            elif i == 1:
                d[score_sorted[i]] = "Silver Medal"
            elif i == 2:
                d[score_sorted[i]] = "Bronze Medal"
            else:
                d[score_sorted[i]] = str(i+1)
                
        res = []
        for i in score:
            res.append(d[i])
        return res
