class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def traverse(currIndex):
            if currIndex >= len(stoneValue):
                return 0
                
            choose1 = float('-inf')
            choose2 = float('-inf')
            choose3 = float('-inf')
            choose1 = stoneValue[currIndex] - traverse(currIndex + 1)
            
            if currIndex + 1 < len(stoneValue):
                choose2 = (stoneValue[currIndex] + stoneValue[currIndex + 1]) - traverse(currIndex + 2)
            
            if currIndex + 2 < len(stoneValue):
                choose3 = (stoneValue[currIndex] + stoneValue[currIndex + 1] + stoneValue[currIndex + 2]) - traverse(currIndex + 3)
                
            currScore = (max(choose1, choose2, choose3))
            return currScore
            
        ans = traverse(0)
        # print(ans)
        if ans > 0:
            return "Alice"
        if ans == 0:
            return "Tie"
        return "Bob"