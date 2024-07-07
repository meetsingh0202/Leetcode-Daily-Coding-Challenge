class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        emptyBottles = 0

        while numBottles > 0:
            print(numBottles, emptyBottles)
            count += numBottles
            emptyBottles += numBottles 
        
            numBottles = emptyBottles // numExchange 
            emptyBottles = emptyBottles % numExchange 

        return count
