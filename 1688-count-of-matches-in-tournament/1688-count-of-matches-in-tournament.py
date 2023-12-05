class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        currTeams = n
        currMatches = 0
        
        while currTeams != 1:
            
            if currTeams % 2 == 1:
                tempMatches = currTeams // 2
                currMatches += tempMatches
                currTeams = currTeams // 2 + 1
            else:
                tempMatches = currTeams // 2
                currMatches += tempMatches
                currTeams = currTeams // 2
        
        return currMatches