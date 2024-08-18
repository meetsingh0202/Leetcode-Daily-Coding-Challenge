class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<6:
            return n
        
        l = [1]
        n -= 1
        while (n):
            temp = l[0]
            
            l=l[1:]
            l=set(l)
            l.add(temp*2)
            l.add(temp*3)
            l.add(temp*5)
            l=list(l)
            l.sort()
            n-=1
        return l[0]