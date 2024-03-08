class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        HashMap = dict()
        total = 0
        MaxFreq = 0
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
        
        for key, val in HashMap.items():
            MaxFreq = max(MaxFreq, val)
        
        for key, val in HashMap.items():
            if val == MaxFreq:
                total += val
            
        return total