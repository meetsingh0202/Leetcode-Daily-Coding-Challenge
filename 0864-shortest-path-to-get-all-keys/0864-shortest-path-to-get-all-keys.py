class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        def check(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] =='#':
                return False
            return True
        
        queue = deque([])
        totalKeys = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0, "", 0))
                if grid[i][j] in string.ascii_lowercase:
                    totalKeys += 1
                        
        while queue:
            # print(queue)
            for i in range(len(queue)):
                row, col, currScore, currKeys, keys, currSteps = queue.popleft()
                
                if currKeys == totalKeys:
                    return currScore
                
                if currSteps >= ROWS * COLS:
                    continue 
                    
                if (row, col, keys) in visited:
                    continue
                    
                visited.add((row, col, keys))
                    
                for i in directions:
                    r, c = row + i[0], col + i[1]
                    
                    if check(r, c):
                        currChar = grid[r][c]
                        if currChar in string.ascii_lowercase:
                            if currChar not in keys:
                                queue.append((r, c, currScore + 1, currKeys + 1, keys + currChar, currSteps + 1))
                            else:
                                queue.append((r, c, currScore + 1, currKeys, keys, currSteps + 1))
                                
                        elif currChar in string.ascii_uppercase:
                            if currChar.lower() not in keys:
                                continue
                            else:
                                queue.append((r, c, currScore + 1, currKeys, keys, currSteps + 1))
                                
                        else:
                            queue.append((r, c, currScore + 1, currKeys, keys, currSteps + 1))
                            
        return -1