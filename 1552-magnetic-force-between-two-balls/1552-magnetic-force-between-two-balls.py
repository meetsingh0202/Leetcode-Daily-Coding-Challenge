class Solution:
    def canDistributebykeepingMidDistance(self,position,m,mid):
        placed_balls = 1
        placed_index = 0
        for i in range(0, len(position)):
            if position[i] - position[placed_index] >= mid:
                placed_balls += 1
                placed_index = i
        return placed_balls >= m
        
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = sys.maxsize
        ans = low
        while low <= high:
            mid = (low + high) >> 1
            if self.canDistributebykeepingMidDistance(position, m, mid):
                ans = mid
                low = mid + 1 
            else:
                high = mid - 1
        return ans