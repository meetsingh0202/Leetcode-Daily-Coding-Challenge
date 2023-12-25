class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(s, memo, index) -> int:
            if index in memo:
                return memo[index]
            if index == len(s):
                memo[index] = 1
                return 1
            if index > len(s) or s[index] == '0':
                return 0
            
            count = dfs(s, memo, index + 1)
            if index + 1 <= len(s) and int(s[index:index + 2]) <= 26:
                count += dfs(s, memo, index + 2)
                
            memo[index] = count
            return count
        
        return dfs(s, memo, 0)