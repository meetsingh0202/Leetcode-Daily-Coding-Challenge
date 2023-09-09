class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def traverse(target):            
            if target in memo:
                return memo[target]
            
            if target==0:
                return 1
            if target<0:
                return 0
            
            ways=0
            for i in nums:
                temp=target-i
                if temp<0:
                    break
                ways+=traverse(temp)
            
            memo[target]=ways
            return memo[target]
            
        nums.sort()
        memo={0:1}
        traverse(target)
        return memo[target]