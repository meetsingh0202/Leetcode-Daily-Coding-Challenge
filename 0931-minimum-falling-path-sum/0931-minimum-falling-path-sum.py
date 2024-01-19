class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        dp = [[0 for i in range(COLS + 1)] for j in range(ROWS + 1)]
        
        for i in range(COLS + 1):
            dp[0][i] = float('inf')
            
        for i in range(ROWS + 1):
            dp[i][0] = float('inf')
            
        for i in range(COLS):
            dp[-1][i + 1] = matrix[-1][i]
            
        for i in range(ROWS):
            dp[1][i + 1] = matrix[0][i]
        
        for row in range(2, ROWS + 1):
            for col in range(1, COLS + 1):
                r, c = row - 1, col - 1
                currElement = matrix[r][c]
                
                diagonal1 = dp[row - 1][col - 1]
                    
                down = dp[row - 1][col]
                
                if col + 1 < len(dp[0]):
                    diagonal2 = dp[row - 1][col + 1]
                else:
                    diagonal2 = float('inf')
                
                dp[row][col] = currElement + min(diagonal1, down, diagonal2)
        
        return min(dp[-1])
                
                
            
        
        