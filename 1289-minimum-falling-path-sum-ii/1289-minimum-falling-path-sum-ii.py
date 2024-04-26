class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def traverse(currRow, lastCol):
            
            if currRow == ROWS:
                return 0
            
            res = float('inf')
            
            for i in range(COLS):
                if i != lastCol:
                    res = min(res, grid[currRow][i] + traverse(currRow + 1, i))
            
            return res
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        return traverse(0, -1)