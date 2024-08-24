class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        def smaller(firsthalf):
            firsthalf=str(int(firsthalf)-1)
            total=firsthalf+firsthalf[-1-isOdd::-1]
            return int(total)
            
        def equal(firsthalf):
            total=firsthalf+firsthalf[-1-isOdd::-1]
            # print(firsthalf)
            # print(firsthalf[-1-isOdd::-1])
            return int(total)
            
        def greater(firsthalf):
            firsthalf=str(int(firsthalf)+1)
            total=firsthalf+firsthalf[-1-isOdd::-1]
            return int(total)
            
        isOdd=len(n)&1
        low, high = 10 ** (len(n) - 1) - 1, 10 ** len(n) + 1
        firsthalf=n[:(len(n)//2)+isOdd]
        smallerThanN=smaller(firsthalf)
        equalToN=equal(firsthalf)
        greaterThanN=greater(firsthalf)
        n=int(n)
        diffa=int(n)-smallerThanN
        diffb=0
        diffc=greaterThanN-int(n)
        diffd=high-int(n)
        diffe=int(n)-low
        # print(smallerThanN,equalToN,greaterThanN)
        # print(diffa,diffb,diffc,diffd,diffe)
        
        if equalToN == int(n):
            return str(min([low, high, smallerThanN, greaterThanN],key=lambda x:(abs(x-n), x)))
        else:
            return str(min(
                [low, high, smallerThanN, equalToN, greaterThanN],
                key=lambda x: (abs(x - n), x)))