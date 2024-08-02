class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        windows_size = sum(nums)
        result = current_zero = windows_size - sum(nums[:windows_size])
        for i in range(n):
            if nums[(i + windows_size) %  n] == 0:
                current_zero += 1
            if nums[i] == 0:
                current_zero -= 1
            result = min(result, current_zero)
        return result
