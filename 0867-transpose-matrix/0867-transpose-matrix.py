class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[]
        for i in range(len(matrix[0])):
            list1=[]
            for j in range(len(matrix)):
                list1.append(matrix[j][i])
            transposed.append(list1)
        return (transposed)