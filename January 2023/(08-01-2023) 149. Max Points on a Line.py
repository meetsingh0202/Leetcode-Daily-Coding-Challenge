class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        res=0
        
        for index1,currPoint in enumerate(points):
            currSlopes = defaultdict(int)
            x1=currPoint[0]
            y1=currPoint[1]
            for index2,nextPoint in enumerate(points[index1+1:]):
                x2=nextPoint[0]
                y2=nextPoint[1]
                slope = (y2-y1)/(x2-x1) if x1!=x2 else float('inf')
                currSlopes[slope]+=1
                res=max(res,currSlopes[slope])
            # print(currSlopes)
        return res+1
