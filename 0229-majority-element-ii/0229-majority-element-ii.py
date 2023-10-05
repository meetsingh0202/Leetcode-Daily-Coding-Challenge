class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidate1,candidate2,count1,count2=None,None,0,0
        
        for i in nums:
            if i==candidate1:
                count1+=1
                continue
            if i==candidate2:
                count2+=1
                continue
            if count1==0:
                candidate1=i
                count1=1
                continue
            if count2==0:
                candidate2=i
                count2=1
                continue
            count1-=1
            count2-=1
            
        res = []
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)
        
        if count1 > len(nums)//3:
            res.append(candidate1)
            
        if count2 > len(nums)//3:
            res.append(candidate2)
        
        return res