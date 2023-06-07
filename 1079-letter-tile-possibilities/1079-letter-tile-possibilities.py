class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        
        def traverse(s):
            if len(s) > 0:
                visitedChars.add(s)
            
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    traverse(s + tiles[i])
                    visited.remove(i)
        
        visitedChars = set()
        visited = set()
        n = len(tiles)
        
        traverse("")
        
        return len(visitedChars)