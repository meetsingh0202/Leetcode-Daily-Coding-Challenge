class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp = [[0 for _ in range(n + 1)] for i in range(m + 1)]
        
        # dp[0][1] = 1
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
            elif obstacleGrid[0][i] == 1:
                    obstacleGrid[0][i] = 0
                    
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            elif obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return (obstacleGrid[-1][-1])