class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        
        prefix = [0 for i in range(n)]
        
        for i in bookings:
            start, end, val = i
            
            start -= 1
            end -= 1
            
            prefix[start] += val
            
            if end + 1 < n:
                prefix[end + 1] -= val
            
            # print(prefix)
            
        res = []
        currSum = 0
        
        for i in prefix:
            currSum += i
            res.append(currSum)
        
        return res