class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_rows, n_cols = len(grid), len(grid[0])
        
        thieves_grids = deque((r, c) for r in range(n_rows) for c in range(n_cols) if grid[r][c] == 1)
        grid = [[0 if cell == 1 else -1 for cell in row] for row in grid]
        
        while thieves_grids:
            for _ in range(len(thieves_grids)):
                row, col = thieves_grids.popleft()
                value = grid[row][col]
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == -1:
                        grid[nr][nc] = value + 1
                        thieves_grids.append((nr, nc))
        
        priority_queue = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1
        while priority_queue:
            safeness, row, col = heappop(priority_queue)
            if (row, col) == (n_rows - 1, n_cols - 1):
                return -safeness
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] != -1:
                    heappush(priority_queue, (-min(-safeness, grid[nr][nc]), nr, nc))
                    grid[nr][nc] = -1
        return -1
