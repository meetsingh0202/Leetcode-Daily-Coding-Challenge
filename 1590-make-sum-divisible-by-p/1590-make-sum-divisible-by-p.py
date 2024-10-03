class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        Totalsum=sum(nums)
        
        if Totalsum%p==0:
            return 0
        
        extraSum=Totalsum%p
        HashMap=dict()
        HashMap[0]=-1
        res=len(nums)
        val=0
        for i in range(len(nums)):
            val=(val+nums[i])%p
            temp=(val-extraSum)%p
            
            if temp<0:
                temp+=p
                
            if temp in HashMap:
                res=min(res,i-HashMap[temp])
            HashMap[val]=i
            
        return -1 if res==len(nums) else res