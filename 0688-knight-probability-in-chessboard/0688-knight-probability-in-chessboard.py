class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def traverse(row, col, k):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return 0
            if k == 0:
                return 1
            # visited.add((row, col))
            d1 = traverse(row - 2, col - 1, k - 1) 
            d2 = traverse(row - 2, col + 1, k - 1)
            d3 = traverse(row - 1, col + 2, k - 1)
            d4 = traverse(row - 1, col - 2, k - 1)
            d5 = traverse(row + 1, col - 2, k - 1)
            d6 = traverse(row + 1, col + 2, k - 1)
            d7 = traverse(row + 2, col - 1, k - 1)
            d8 = traverse(row + 2, col + 1, k - 1)
            # visited.remove((row, col))
            return (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8) / 8
        
        visited = set()
        ROWS = n
        COLS = n
        count = traverse(row, column, k)
        return count