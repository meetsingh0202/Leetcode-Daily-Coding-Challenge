class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        maxDistance = 0
        
        for i in left:
            maxDistance = max(maxDistance, i)
        
        for i in right:
            maxDistance = max(maxDistance, n - i)
        
        return maxDistance
        