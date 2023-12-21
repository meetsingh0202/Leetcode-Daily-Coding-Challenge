class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        res = 0
        prev = points[0][0]
        
        for i in points[1:]:
            curr = i[0]
            
            if curr > prev:
                res = max(res, curr - prev)
                prev = curr
            
        return res