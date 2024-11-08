class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = 2 ** maximumBit - 1
        results = list()
        for num in nums:
            max_val ^= num
            results.append(max_val)
            
        return results[::-1]