class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        print(d)
        rounds = 0
        for i in list(d.values()):
            if i < 2:
                return -1
            else:
                val1 = float('inf')
                val2 = float('inf')
                val3 = float('inf')
                if i % 2 == 0:
                    val1 = i // 2
                if i % 3 == 0:
                    val2 = i // 3
                else:
                    val3 = (i // 3) + 1
                rounds += min(val1, val2, val3)
        return rounds
                    
        
