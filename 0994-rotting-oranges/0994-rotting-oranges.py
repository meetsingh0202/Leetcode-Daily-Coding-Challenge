class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def checkBoundary(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            return True
        
        res = 0
        queue = deque([])
        
        ROWS, COLS = len(grid), len(grid[0])
        
        rotten = set()
        totalOranges = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    rotten.add((i, j))
                    totalOranges += 1
                
                if grid[i][j] == 1:
                    totalOranges += 1
        
        if totalOranges - len(rotten) == 0:
            return 0
        
        while queue:
            for i in range(len(queue)):
                
                row, col = queue.popleft()
                
                for ir, ic in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    r = row + ir
                    c = col + ic
                    
                    if checkBoundary(r, c) and (r, c) not in rotten and grid[r][c] == 1:
                        rotten.add((r, c))
                        queue.append([r, c])
            res += 1
        
            if len(rotten) == totalOranges:
                break
                
        if len(rotten) == totalOranges:
            return res
        
        return -1
            