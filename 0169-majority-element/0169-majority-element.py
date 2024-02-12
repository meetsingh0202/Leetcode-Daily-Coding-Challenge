class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        i=0
        j=1
        while i<len(nums)-1 and j<len(nums):
            if nums[i]!=nums[j]:
                count-=1
                if count==0:
                    i=j
                    count=1
                j+=1
                continue
            elif nums[i]==nums[j]:
                count+=1
                j+=1
        index=i
        count=0
        for i in nums:
            if i==nums[index]:
                count+=1
        if count>len(nums)//2:
            return nums[index]
        return -1
        