class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        count = 0
        diff = high - low 
        if low % 2 == 0 and high % 2 == 0:
            count += diff // 2    
            
        elif low % 2 == 0 and high % 2 == 1:
            count += 1
            count += diff // 2

        elif low % 2 == 1 and high % 2 == 0:
            count += 1
            count += diff // 2

        else:
            count += 2
            diff -= 2
            count += diff // 2

        return count
