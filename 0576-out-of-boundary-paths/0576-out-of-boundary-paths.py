class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        def traverse(row, col, moves):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return 1
            
            if (row, col, moves) in memo:
                return memo[(row, col, moves)]
            
            if moves > 0:
                c1 = traverse(row + 1, col, moves - 1)
                c2 = traverse(row - 1, col, moves - 1)
                c3 = traverse(row, col + 1, moves - 1)
                c4 = traverse(row, col - 1, moves - 1)
                memo[(row, col, moves)] = c1 + c2 + c3 + c4
            else:
                memo[(row, col, moves)] = 0
            return memo[(row, col, moves)] % MOD
        
        ROWS = m
        COLS = n
        MOD = 1000000007
        memo = dict()
        return traverse(startRow, startColumn, maxMove) % MOD
                