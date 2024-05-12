class Solution1:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        rowHeap = []
        colHeap = []
        ROWS, COLS = len(grid), len(grid[0])
        
        for i in range(3):
            for j in range(3):
                currVal = grid[i][j]
                heappush(rowHeap, [-currVal, i])
                heappush(colHeap, [-currVal, j])
        
        res = []
        res.append(max(-rowHeap[0][0], -colHeap[0][0]))
        
        for i in range(1, ROWS - 1):
            
            while rowHeap and rowHeap[0][1] < i:
                heappop(rowHeap)
                
            for j in range(1, COLS - 1):

                while colHeap and colHeap[0][1] < j:
                    heappop(colHeap)
                
                currVal = grid[i][j]
                heappush(rowHeap, [-currVal, i])
                heappush(colHeap, [-currVal, j])
                
                currMaxValRow = -rowHeap[0][0]
                currMaxValCol = -colHeap[0][0]
                res.append(max(currMaxValRow, currMaxValCol))
                
                print(i, j)
                print("ROW HEAP : ", rowHeap)
                print("COL HEAP : ", colHeap)
                print("MAX VAL : ", max(currMaxValRow, currMaxValCol))
            
            # print("CURR ARR : ", res)
            
        resROWS = ROWS - 2
        resCOLS = COLS - 2
        currIndex = 0
        
        arr = []
        for i in range(resROWS):
            tempArr = []
            for j in range(resCOLS):
                tempArr.append(res[currIndex])
                currIndex += 1
            arr.append(tempArr)
                
        return arr
    
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for i in range(n-2)]

        for i in range(1,n-1):
            for j in range(1,n-1):
                maxLocal[i-1][j-1] = max(maxLocal[i-1][j-1],grid[i-1][j],grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j],grid[i+1][j+1],grid[i+1][j-1],grid[i][j-1],grid[i][j],grid[i][j+1])

        return maxLocal
