class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)
        
        count=0
        MaxElement=arr[0]
        
        for i in arr[1:]:
            if MaxElement>i:
                count+=1
            else:
                MaxElement=i
                count=1
            if count==k:
                return MaxElement
        return MaxElement