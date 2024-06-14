class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        
        count = 0
        HashMap = dict()
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        HashMap = dict(sorted(HashMap.items(), key=lambda item: item[0]))
        
        available = []
        Min = min(nums)
        diff = max(nums) + len(nums) + min(nums)
        
        for i in range(Min, Min + diff):
            if i not in HashMap:
                available.append(i)
        available.sort(reverse = True)
            
        for key, val in HashMap.items():
            if val > 1:
                for i in range(val - 1):
                    currReplacement = available.pop()
                    while currReplacement < key:
                        currReplacement = available.pop()
                    count += abs(currReplacement - key)
                    
        return count