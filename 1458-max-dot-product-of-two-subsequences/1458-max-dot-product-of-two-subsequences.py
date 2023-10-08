class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        d={}
        def dfs(i,j):
            if i==len(nums1) or j==len(nums2):return 0
            if (i,j ) in d:return d[(i,j)]
            d[(i,j)]=nums1[i]*nums2[j]
            if i+1<len(nums1) and j+1<len(nums2):
                a=dfs(i+1,j+1)
                d[(i,j)]=max(d[(i,j)]+a,a,d[(i,j)])
            if i+1<len(nums1):d[(i,j)]=max(d[(i,j)],dfs(i+1,j))
            if j+1<len(nums2):d[(i,j)]=max(d[(i,j)],dfs(i,j+1))
            return d[(i,j)]
        return dfs(0,0)