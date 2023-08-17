class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        res = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    res[row][col] = 0
                    continue
                up = res[row - 1][col] if row > 0 else float('inf')
                left = res[row][col - 1] if col > 0 else float('inf')
                res[row][col] = 1 + min(up, left)
                
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if mat[row][col] == 0:
                    res[row][col] = 0
                    continue
                down = res[row + 1][col] if row < ROWS - 1 else float('inf')
                right = res[row][col + 1] if col < COLS - 1 else float('inf')   
                res[row][col] = min(res[row][col], 1 + min(down, right))        
        return res
