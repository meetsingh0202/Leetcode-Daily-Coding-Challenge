class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        s_number = 0
        result = 1
        prev = -1

        modulo = 1_000_000_007
        
        for i, elem in enumerate(corridor):
            if elem == 'S':
                s_number += 1
                if s_number % 2 == 1 and s_number != 1:
                    result = result * (i - prev) % modulo
                prev = i
        
        if s_number == 0 or s_number % 2 == 1:
            return 0
        return result % modulo