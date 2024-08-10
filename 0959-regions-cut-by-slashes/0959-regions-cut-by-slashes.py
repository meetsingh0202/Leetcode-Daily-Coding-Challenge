class Solution:
    def count_regions(self,grid,r,c,n_rows,n_cols):
        if not grid:
            return
        if r<0 or r>=n_rows or c<0 or c>=n_cols or grid[r][c]!=0:
            return
        grid[r][c]=1
        self.count_regions(grid,r+1,c,n_rows,n_cols)
        self.count_regions(grid,r,c+1,n_rows,n_cols)
        self.count_regions(grid,r-1,c,n_rows,n_cols)
        self.count_regions(grid,r,c-1,n_rows,n_cols)

    def regionsBySlashes(self, grid: List[str]) -> int:
        grid = [list(ch) for ch in grid]
        n_cols  = len(grid[0])
        n_rows = len(grid)
        ans = 0
        scaled_grid = [[0 for _ in range(n_cols*3)] for _ in range(n_rows*3)]
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c]=="/":
                    for k in range(3):
                        scaled_grid[r*3+k][c*3+2-k]=1
                elif grid[r][c]=="\\":
                    for k in range(3):
                        scaled_grid[r*3+k][c*3+k]=1
        n_rows = len(scaled_grid)
        n_cols = len(scaled_grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if scaled_grid[r][c]==0:
                    self.count_regions(scaled_grid,r,c,n_rows,n_cols)
                    ans+=1
        return ans
