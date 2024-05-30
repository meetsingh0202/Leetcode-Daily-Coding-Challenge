class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        res=0
        for i in range(n-1):
            cur_xor=arr[i]
            for k in range(i+1,n):
                cur_xor^=arr[k]
                if cur_xor==0:
                    res+=(k-i)
        return res
