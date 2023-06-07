class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def traverse(s):
            if sum(s) == 0:
                return 0

            if (tuple(s) in memo):
                return memo[tuple(s)]
            
            count = 0
        
            for index in range(len(s)):
                if s[index]:
                    s[index] -= 1
                    count += (1 + traverse(s))
                    s[index] += 1
                    
            memo[tuple(s)] = count
            return count
        
        n = len(tiles)
        HashMap = dict()
        
        for i in tiles:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        memo = dict()
        
        return traverse(list(HashMap.values()))