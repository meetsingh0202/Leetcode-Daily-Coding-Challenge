class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        HashMap = dict()
        total = 0
        MaxFreq = 0
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
            MaxFreq = max(MaxFreq, HashMap.get(i, 0))

        for key, val in HashMap.items():
            if val == MaxFreq:
                total += val
            
        return total