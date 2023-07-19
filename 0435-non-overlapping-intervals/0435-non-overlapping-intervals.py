class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        
        count=0
        prevstart=intervals[0][0]
        prevend=intervals[0][1]
        new=[intervals[0]]
        for i in intervals[1:]:
            
            currstart=i[0]
            currend=i[1]
            if currstart<prevend:
                count+=1
                continue
            new.append(i)
            prevstart=new[-1][0]
            prevend=new[-1][1]
        
        return count
                
            