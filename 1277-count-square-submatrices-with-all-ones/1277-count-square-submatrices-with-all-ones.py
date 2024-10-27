class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[0 for i in range(COLS)] for j in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLS):
                
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        res = 0
        for i in dp:
            res += sum(i)
            # print(i)
            
        return res