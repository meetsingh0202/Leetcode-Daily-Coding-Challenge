class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def traverse(currIndex, M):
            if currIndex >= len(piles):
                return 0
            
            if currIndex + 2 * M >= len(piles):
                return sum(piles[currIndex : ])
            
            maxCost = 0
            
            for i in range(1, min(2 * M + 1, len(piles))):
                tempCost = sum(piles[currIndex : ]) - traverse(currIndex + i, max(M, i))
                maxCost = max(maxCost, tempCost)
                
            return maxCost 
        
        return traverse(0, 1)
