class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        def traverse(row1,col1,row2,col2):
            if row1<0 or row1>=ROWS or row2<0 or row2>=ROWS or col1<0 or col1>=COLS or col2<0 or col2>=COLS:
                return float('-inf')
            
            if row1==ROWS-1 and row2==ROWS-1:
                if col1==col2:
                    return grid[row1][col1]
                else:
                    return grid[row1][col1]+grid[row1][col2]
            
            if (row1,col1,row2,col2) in memo:
                return memo[(row1,col1,row2,col2)]
            
            maxcount=float('-inf')
            for i in range(-1,2):
                for j in range(-1,2):
                    value=0
                    if col1==col2:
                        value=grid[row1][col1]
                    else:
                        value+=grid[row1][col1]+grid[row2][col2]
                    value+=traverse(row1+1,col1+i,row2+1,col2+j)
                    maxcount=max(maxcount,value)
                    
            memo[(row1,col1,row2,col2)]=maxcount
            return memo[(row1,col1,row2,col2)]
            
        memo={}
        ROWS=len(grid)
        COLS=len(grid[0])
        memo={}
        return traverse(0,0,0,COLS-1)