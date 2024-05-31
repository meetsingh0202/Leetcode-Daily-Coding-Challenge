class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_nums = 0
        for num in nums:
            xor_nums ^= num
        
        tempxor=xor_nums&(-xor_nums)
        second_xor=0

        for i in nums:
            if (tempxor&i):
                second_xor^=i
            
        return [second_xor,second_xor^xor_nums]