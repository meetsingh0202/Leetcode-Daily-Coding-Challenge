class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(n):
            n = str(n)
            n = n[::-1]
            return int(n)
        
        MOD = 10**9 + 7
        HashMap = dict()
        count = 0
        for i in range(len(nums)):
            temp = nums[i] - reverse(nums[i])
            if temp in HashMap:
                count += HashMap[temp]
                HashMap[temp]+=1
            else:
                HashMap[temp] = 1
                
        return count % MOD
    