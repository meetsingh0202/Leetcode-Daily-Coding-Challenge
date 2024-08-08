class Solution:
    def spiralMatrixIII(self, ROWS: int, COLS: int, rStart: int, cStart: int) -> List[List[int]]:
        
        def CheckBoundary(row,col):
            if row<0 or row>=ROWS or col<0 or col>=COLS:
                return False
            return True
        
        res=[[rStart,cStart]]
        
        Turn=1
        
        row,col=rStart,cStart
        
        while True:
            # print(row,col)
            if len(res)==(ROWS*COLS):
                return res
            
            for _ in range(Turn):
                col+=1
                if CheckBoundary(row,col):
                    # print(row,col)
                    res.append([row,col])
            
            for _ in range(Turn):
                row+=1
                if CheckBoundary(row,col):
                    # print(row,col)
                    res.append([row,col])
            
            for _ in range(Turn+1):
                col-=1
                if CheckBoundary(row,col):
                    res.append([row,col])
            
            for _ in range(Turn+1):
                row-=1
                if CheckBoundary(row,col):
                    res.append([row,col])
            
            Turn+=2
            
            