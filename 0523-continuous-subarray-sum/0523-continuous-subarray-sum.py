class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        set_ = set()
        prev = 0
        curr = 0
        for each in nums:
            curr += each
            curr %= k
            if curr in set_:
                return True
            set_.add(prev)
            prev = curr
        return False