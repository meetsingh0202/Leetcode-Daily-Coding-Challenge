class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        
        def check(currColor):
            startRow, endRow, startCol, endCol = componentIndexes[currColor]
            flag = True
            
            for i in range(startRow, endRow + 1):
                for j in range(startCol, endCol + 1):
                    if targetGrid[i][j] != currColor and targetGrid[i][j] != '#':
                        flag = False
                        break
                        
            if flag:
                for i in range(startRow, endRow + 1):
                    for j in range(startCol, endCol + 1):
                        targetGrid[i][j] = '#'
            
            return flag
            
        ROWS, COLS = len(targetGrid), len(targetGrid[0])
        
        componentIndexes = dict()
        allColors = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                currColor = targetGrid[i][j]
                allColors.add(currColor)
                if currColor not in componentIndexes:
                    componentIndexes[currColor] = [float('inf'), float('-inf'), float('inf'), float('-inf')]
                    componentIndexes[currColor][0] = min(componentIndexes[currColor][0], i)
                    componentIndexes[currColor][1] = max(componentIndexes[currColor][1], i)
                    componentIndexes[currColor][2] = min(componentIndexes[currColor][2], j)
                    componentIndexes[currColor][3] = max(componentIndexes[currColor][3], j)
                else:
                    componentIndexes[currColor][0] = min(componentIndexes[currColor][0], i)
                    componentIndexes[currColor][1] = max(componentIndexes[currColor][1], i)
                    componentIndexes[currColor][2] = min(componentIndexes[currColor][2], j)
                    componentIndexes[currColor][3] = max(componentIndexes[currColor][3], j)
                    
        while allColors:
            tempColors = set()
            
            for i in allColors:
                # print(i, check(i))
                
                if not check(i):
                    tempColors.add(i)
            
            if len(tempColors) == len(allColors):
                return False
            allColors = tempColors
            
        return len(allColors) == 0