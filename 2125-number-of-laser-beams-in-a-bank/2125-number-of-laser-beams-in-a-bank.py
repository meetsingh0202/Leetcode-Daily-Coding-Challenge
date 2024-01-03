class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prefix = []
        ROWS, COLS = len(bank), len(bank[0])
        
        for i in range(ROWS):
            curr = 0
            for j in range(COLS):
                if bank[i][j] == '1':
                    curr += 1
            if curr:
                prefix.append(curr)
        
        if not prefix:
            return 0
            
        count = 0
        prev = prefix[0]
        
        for i in prefix[1:]:
            curr = i
            count += (curr * prev)
            prev = curr
        
        return count