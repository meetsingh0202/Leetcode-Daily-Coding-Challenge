class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if nums==[0]:
            return [0]
        
        if nums==[0,1]:
            return [0,1]
        
        def check(n):
            if n==0:
                return True
            if n%2==0:
                return True
            return False
        
        i=0
        j=len(nums)-1
        while i<len(nums) and j>0:    
            c=0
            if i>j:
                break
            if check(nums[i])==True:
                i+=1
                c=1
            if check(nums[j])==False:
                j-=1
                c=1
            if c==1:
                continue
            if check(nums[i])!=check(nums[j]):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
                continue
            if check(nums[i])==True:
                i+=1
            if check(nums[j])==False:
                j-=1
        return (nums)
            