class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        temp=sorted(enumerate(nums),key=lambda x:x[1])
        output=0
        idx=temp[0][0]
        for i,n in temp:
            if i<idx:
                idx=i
            else:
                output=max(output,i-idx)
        return output
            