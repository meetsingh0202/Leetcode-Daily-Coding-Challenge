class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def calculateXY(val):
            nextVal = val + 1
            if nextVal % ROWS == 0:
                nextX = nextVal // ROWS
                nextY = nextVal % ROWS
                direction = nextVal // ROWS
                if direction % 2 == 1:
                    return ROWS - nextX, COLS - nextY - 1
                else:
                    return ROWS - nextX, nextY 
                
            direction = math.ceil(nextVal / ROWS)
            nextX = nextVal // ROWS
            nextY = nextVal % ROWS
            if direction % 2 == 0:
                return ROWS - 1 - nextX, COLS - nextY 
            else:
                return ROWS - 1 - nextX, nextY - 1
            
        
        ROWS = len(board)
        COLS = len(board[0])
        queue = deque([[1, 0, 0]])
        target = ROWS * COLS
        Min = float('inf')
        visited = set()
        finalFlag = False
        while queue:
            # print(queue)
            currVal, count, flag = queue.popleft()
            if currVal == target:
                Min = min(Min, count)
                finalFlag = True
                continue
                
            if count > target:
                continue
            if finalFlag and count >= Min:
                continue
            row, col = calculateXY(currVal - 1)
            boardVal = board[row][col]
                
            
            if boardVal != -1 and (flag != 'L' and flag != 'S'):
                if boardVal == target:
                    Min = min(Min, count)
                    finalFlag = True
                    continue
                    
                if currVal < boardVal and flag != 'L':
                    if (boardVal, count) not in visited:
                        queue.append([boardVal, count, 'L'])
                        visited.add((boardVal, count, 'L'))
                        
                elif currVal > boardVal and flag != 'S':
                    if (boardVal, count) not in visited:
                        queue.append([boardVal, count, 'S'])
                        visited.add((boardVal, count, 'S'))
            
            if boardVal == -1 or (boardVal != -1 and (flag == 'L' or flag == 'S')):
                if currVal == target:
                    Min = min(Min, count)
                    finalFlag = True
                    continue
                for i in range(1, 7):
                    if currVal + i <= ROWS * COLS and (currVal + i, count + 1, 1) not in visited:
                        queue.append([currVal + i, count + 1, 1])
                        visited.add((currVal + i, count + 1, 1))
                        
        return Min if Min != float('inf') else -1 
