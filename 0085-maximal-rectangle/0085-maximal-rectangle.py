class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nextRightSmallerElement(arr, n):
            stack = []
            res = [-1]*n
            for i in range(n - 1 , -1 , -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    res[i] = n
                else:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        
        def nextLeftSmallerElement(arr, n):
            stack = []
            res = [-1]*n
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    res[i] = -1
                else:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        
        right = nextRightSmallerElement(heights, len(heights))
        left = nextLeftSmallerElement(heights, len(heights))
        res = 0
        
        for i in range(len(heights)):
            temp = (right[i] - left[i] - 1) * heights[i]
            res = max(res, temp)
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rectangle = [[0 for i in range(COLS)] for j in range(ROWS)]
        
        for i in range(COLS):
            if matrix[0][i] == '1':
                rectangle[0][i] = 1
            else:
                rectangle[0][i] = 0
        
        for i in range(1, ROWS):
            for j in range(COLS):
                prev = rectangle[i - 1][j]
                if matrix[i][j] == '1':
                    rectangle[i][j] = 1 + prev
                else:
                    rectangle[i][j] = 0
                    
        res = 0
        for i in rectangle:
            currRow = i
            res = max(res, self.largestRectangleArea(currRow))
        return res
            