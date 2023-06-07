class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        @cache
        def traverse(s):
            if s == '0' * len(s):
                return 0

            if (s in memo):
                return memo[s]
            
            count = 0
        
            for index in range(len(s)):
                if s[index] != '0':
                    s = s[:index] + str(int(s[index]) - 1) + s[index + 1: ]
                    count += (1 + traverse(s))
                    s = s[:index] + str(int(s[index]) + 1) + s[index + 1: ]
                    
            memo[s] = count
            return count
        
        n = len(tiles)
        HashMap = dict()
        
        for i in tiles:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        memo = dict()
        currS = ""
        
        for i in HashMap.values():
            currS += str(i)
            
        return traverse(currS)