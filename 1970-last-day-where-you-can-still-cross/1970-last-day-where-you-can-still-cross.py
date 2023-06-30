class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def check(mid):
            def traverse(r, c):
                if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited:
                    return False
                
                if r == row - 1:
                    return True
            
                visited.add((r, c))
                
                return traverse(r - 1, c) or traverse(r + 1, c) or traverse(r, c - 1) or traverse(r, c + 1)

            visited = set()

            for i in range(min(mid, len(cells))):
                x, y = cells[i]
                visited.add((x - 1, y - 1))
                
            for i in range(col):
                if traverse(0, i):
                    return True
            return False
            
        
        low = 1
        high = sys.maxsize
        ans = 1
        
        while low <= high:
            mid = (low + high) >> 1
            
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans