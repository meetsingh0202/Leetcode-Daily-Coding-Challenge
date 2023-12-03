class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_travel = 0

        if len(points) == 1:
            return total_travel
        
        for i in range(1,len(points)):
            x = abs(points[i][0] - points[i-1][0])
            y = abs(points[i][1] - points[i-1][1])

            if x > y:
                time = x
            else:
                time = y
            
            total_travel += time

        return total_travel
