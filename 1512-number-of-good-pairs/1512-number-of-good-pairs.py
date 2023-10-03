class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        countPairs = 0
        counter = {}

        for n in nums:
            if n in counter:
                countPairs += counter[n]
                counter[n] += 1
            else:
                counter[n] = 1

        return countPairs