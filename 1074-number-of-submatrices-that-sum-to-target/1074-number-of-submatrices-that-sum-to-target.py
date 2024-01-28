class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        ROWS,COLS=len(matrix),len(matrix[0])
        res=0
        dict1={}
        for row in matrix:
            for i in range(1,len(row)):
                row[i]+=row[i-1]
        
        for start in range(COLS):
            for end in range(start,COLS):
                dict1=defaultdict(int)
                sum1=0
                dict1[0]=1
                for k in range(ROWS):
                    sum1+=matrix[k][end]-(matrix[k][start-1] if start!=0 else 0)
                    if sum1-target in dict1:
                        res+=dict1[sum1-target]
                    dict1[sum1]+=1
        
        return res