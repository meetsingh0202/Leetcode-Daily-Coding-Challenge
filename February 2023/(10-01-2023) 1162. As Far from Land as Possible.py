class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        def calculateDistance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        zeros = []
        ones = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                else:
                    ones.append((i, j))
        
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ans = float('-inf')
        for i in ones:
            q.append([i[0], i[1], float('-inf'), i[0], i[1]])
        
        if len(ones) == 0 or len(ones) == ROWS * COLS:
            return -1
        visited = set()
        
        while q:
            row, col, distance, srow, scol = q.popleft()
            
            if grid[row][col] == 0:
                ans = max(ans, distance)
                
            for i in directions:
                nrow, ncol = row + i[0], col + i[1]
                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS:
                    if (nrow, ncol) not in visited:
                        if grid[nrow][ncol] == 0:
                            visited.add((nrow, ncol))    
                            currDistance = calculateDistance(srow, scol, nrow, ncol)
                            q.append([nrow, ncol, max(distance, currDistance), srow, scol])
            
        return ans if ans != float('-inf') else -1
