class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleocc=0
        twoocc=0
        
        for i in nums:
            singleocc=(~twoocc)&(singleocc^i)
            twoocc=(~singleocc)&(twoocc^i)
        
        return singleocc
    