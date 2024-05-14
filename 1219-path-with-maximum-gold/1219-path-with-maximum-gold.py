class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        res=0
        
        def dfs(row,col,gold):
            if row<0 or col<0 or col>len(grid[0])-1 or row>len(grid)-1 or grid[row][col]==0 or visited[row][col]==True:
                return gold
            
            visited[row][col]=True
            gold+=grid[row][col]
            # print(gold)
            up=dfs(row-1,col,gold)
            down=dfs(row+1,col,gold)
            right=dfs(row,col+1,gold)
            left=dfs(row,col-1,gold)
            visited[row][col]=False
            return max(up,down,left,right)
        
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    temp=dfs(i,j,0)
                    res=max(res,temp)
        return res