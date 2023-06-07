class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        
        def traverse(s):
            nonlocal count
            
            if sum(s) == 0:
                count += 1
                return
            
            count += 1
        
            for index in range(len(s)):
                if s[index]:
                    s[index] -= 1
                    traverse(s)
                    s[index] += 1
        
        n = len(tiles)
        HashMap = dict()
        
        for i in tiles:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        count = 0
        traverse(list(HashMap.values()))
        
        return count - 1