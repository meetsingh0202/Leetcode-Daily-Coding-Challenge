class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower=[]
        for i in range(100):
            temp=[]
            for j in range(i+1):
                temp.append(0)
            tower.append(temp)
        
        tower[0][0]+=poured
        down=0
        while(down<100 and tower[down][(down//2)]>1):
            for i in range(down+1):
                k=tower[down][i]-1
                if(k>0 and down+1<100):
                    tower[down+1][i]+=k/2
                    tower[down+1][i+1]+=k/2
                    tower[down][i]=1
                elif(k>0 and down+1>99):
                    tower[down][i]=1
            down+=1
            
        return tower[query_row][query_glass]