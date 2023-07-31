class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def traverse(index1, index2):
            if index1 == len(s1) and index2 == len(s2):
                return 0
            
            if index1 == len(s1) and index2 != len(s2):
                return ord(s2[index2]) + traverse(index1, index2 + 1)
            
            if index1 != len(s1) and index2 == len(s2):
                return ord(s1[index1]) + traverse(index1 + 1, index2)
            
            if s1[index1] == s2[index2]:
                return traverse(index1 + 1, index2 + 1)
            
            return min((ord(s1[index1]) + traverse(index1 + 1, index2)), (ord(s2[index2]) + traverse(index1, index2 + 1)))
    
        return traverse(0, 0)
    
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] 
        
        for r in range(1, len(s1) + 1):
            dp[r][0] = dp[r - 1][0] + ord(s1[r - 1])
        
        for c in range(1, len(s2) + 1):
            dp[0][c] = dp[0][c - 1] + ord(s2[c - 1])
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
                else:
                    dp[i][j] = min(ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1])
        
        # for i in dp:
        #     print(i)
            
        return dp[-1][-1]