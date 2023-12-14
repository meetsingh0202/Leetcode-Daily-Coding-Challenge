class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        oneRow = dict()
        oneCol = dict()
        zeroRow = dict()
        zeroCol = dict()
        diff = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 0:
                    zeroRow[i] = 1 + zeroRow.get(i, 0)
                    zeroCol[j] = 1 + zeroCol.get(j, 0)                    
                else:
                    oneRow[i] = 1 + oneRow.get(i, 0)
                    oneCol[j] = 1 + oneCol.get(j, 0)
        
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(oneRow.get(i, 0) + oneCol.get(j, 0) - zeroRow.get(i, 0) - zeroCol.get(j, 0))
            diff.append(temp)
        
        return diff