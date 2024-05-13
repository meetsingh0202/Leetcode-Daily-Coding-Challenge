class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        def flipRow(rowNum):
            for j in range(COLS):
                grid[rowNum][j] = 1 if grid[rowNum][j] == 0 else 0

        def flipCol(colNum):
            for i in range(ROWS):
                grid[i][colNum] = 1 if grid[i][colNum] == 0 else 0

        ROWS, COLS = len(grid), len(grid[0])
        
        for i in range(ROWS):
            if grid[i][0] == 0:
                flipRow(i)

        # for i in grid:
        #     print(i)
        
        # print("----------")
        
        for j in range(1, COLS):
            oneCount = 0
            for i in range(ROWS):
                if grid[i][j] == 1:
                    oneCount += 1
                    
            if oneCount < math.ceil(ROWS / 2):
                flipCol(j)
        
        # for i in grid:
        #     print(i)
            
        res = 0
        
        for i in range(ROWS):
            currNum = ""
            for j in range(COLS):
                currNum += str(grid[i][j])
            res += int(currNum, 2)
        
        return res