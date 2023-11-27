class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = defaultdict(list)
        
        moves[0] = [4, 6]
        moves[1] = [8, 6]
        moves[2] = [7, 9]
        moves[3] = [4, 8]
        moves[4] = [0, 3, 9]
        moves[6] = [0, 1, 7]
        moves[7] = [2, 6]
        moves[8] = [1, 3]
        moves[9] = [2, 4]
        
        @cache
        def traverse(currNumber, remainingSize):
            if remainingSize == 0:
                return 1
            if currNumber not in moves:
                return 0
            
            count = 0
            
            for i in moves[currNumber]:
                count += traverse(i, remainingSize - 1) % MOD
            return count % MOD
        
        totalCount = 0
        MOD = 1000000007
        for i in range(10):
            totalCount += traverse(i, n - 1) % MOD
        return totalCount % MOD