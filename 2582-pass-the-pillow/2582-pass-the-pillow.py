class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        currPos = 1
        currTime = 0
        flag = 0
        
        for i in range(time):
            currTime += currPos
            
            if currTime == n:
                currTime = n - 2
                currPos = -1
            elif currTime == -1:
                currTime = 1
                currPos = 1
        
        return currTime + 1
                