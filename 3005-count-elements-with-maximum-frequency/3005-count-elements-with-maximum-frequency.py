class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        HashMap = dict()
        total = 0
        MaxFreq = 0
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
            if HashMap.get(i, 0) > MaxFreq:
                MaxFreq = HashMap.get(i, 0)
                total = HashMap.get(i, 0)
                
            elif HashMap.get(i, 0) == MaxFreq:
                total += HashMap.get(i, 0)
            
        return total