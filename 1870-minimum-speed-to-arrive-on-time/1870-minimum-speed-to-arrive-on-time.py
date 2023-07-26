class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def check(currSpeed):
            tempTime = 0
            for i in range(len(dist)):
                if i == len(dist)-1:
                    tempTime += (dist[i] / currSpeed)
                else:
                    tempTime += ceil(dist[i] /currSpeed)
            return tempTime <= hour
            
        low = 1 
        high = pow(10, 7)
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        if ans <= 10**7 and ans != 0:
            return ans
        return -1