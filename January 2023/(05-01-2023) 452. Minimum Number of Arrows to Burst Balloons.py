class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=1
        x=points[0]
        print(points)
        for i in range(len(points)):
            print(points[i][0], x[1])
            if points[i][0] > x[1]:
                ans += 1
                x = points[i]
        
        return ans
