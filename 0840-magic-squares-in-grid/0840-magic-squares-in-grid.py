class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        COLS, ROWS = len(grid[0]), len(grid)
        
        def checkMagicSquare(row, col):
            rowSum = set()
            colSum = set()
            diagonalSum1 = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
            diagonalSum2 = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]
            HashSet = set()
            
            for k in range(row - 1, row + 2):
                for l in range(col - 1, col + 2):
                    val = grid[k][l]
                    if val < 1 or val > 9 or val in HashSet:
                        return False
                    HashSet.add(val)
            
            for k in range(row - 1, row + 2):
                currSum = 0
                for l in range(col - 1, col + 2):
                    currSum += grid[k][l]
                rowSum.add(currSum)
                
                
            for k in range(col - 1, col + 2):
                currSum = 0
                for l in range(row - 1, row + 2):
                    currSum += grid[l][k]
                colSum.add(currSum)
                
            if len(colSum) == 1 and len(rowSum) == 1 and diagonalSum1 == diagonalSum2:
                return True
            return False
        
        totalCount = 0
        
        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if checkMagicSquare(i, j):
                    totalCount += 1
        
        return totalCount