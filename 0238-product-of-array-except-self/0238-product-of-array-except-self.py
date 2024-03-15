class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]
            
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
            
        return res
        """
        prefixproduct=[]
        postfixproduct=[]
        res=[]
        temp=1
        for i in nums:
            temp=temp*i
            prefixproduct.append(temp)
        temp=1
        for i in nums[::-1]:
            temp=temp*i
            postfixproduct.append(temp)
        postfixproduct=postfixproduct[::-1]
        
        for i in range(len(nums)):
            if i==len(nums)-1:
                res.append(prefixproduct[i-1])
                continue
            if i==0:
                res.append(postfixproduct[1])
                continue
            temp=postfixproduct[i+1]*prefixproduct[i-1]
            res.append(temp)
        
        # print(prefixproduct)
        # print(postfixproduct)
        return res
        """
        
            
            