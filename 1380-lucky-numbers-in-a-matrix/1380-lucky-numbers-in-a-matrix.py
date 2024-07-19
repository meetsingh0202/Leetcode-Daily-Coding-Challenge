class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r=[]
        c=[]
        for i in range(len(matrix)):
            r.append(min(matrix[i]))
            
        for i in range(len(matrix[0])):
            list1=[]
            for j in range(len(matrix)):
                list1.append(matrix[j][i])
            c.append(max(list1))
        res=[]
        for i in r:
            if i in c:
                res.append(i)
                break
        return res