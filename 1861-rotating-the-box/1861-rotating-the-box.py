class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        rows, cols = len(box), len(box[0])
        temp = [['.'] * cols for _ in range(rows)]
        res = [['.'] * rows for _ in range(cols)]

        for r in range(rows):
            last_empty = cols - 1
            for c in range(cols - 1, -1, -1):
                
                if box[r][c] == '#':
                    temp[r][last_empty] = '#'
                    last_empty -= 1
                    
                elif box[r][c] == '*':
                    temp[r][c] = '*'
                    last_empty = c - 1
        
        for i in range(rows):
            for j in range(cols):
                res[j][i] = temp[rows - 1 - i][j]
            
        return res
