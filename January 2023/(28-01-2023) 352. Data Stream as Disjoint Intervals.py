class SummaryRanges:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, val: int) -> None:
        if val in self.arr:
            return
        arr=self.arr
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if arr[mid]>val:
                hi=mid-1
            else:
                lo=mid+1
        arr.insert(lo,val)
        

    def getIntervals(self) -> List[List[int]]:
        arr=self.arr
        ans=set()
        start=end=0
        while end<len(arr):
            while end+1<len(arr) and arr[end+1]-arr[end]==1:
                end+=1
            ans.add((arr[start],arr[end]))
            end+=1
            start=end
        return sorted(list(ans))
