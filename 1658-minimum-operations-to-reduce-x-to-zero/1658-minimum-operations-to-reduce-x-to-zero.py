class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        arr_sum = sum(nums)
        if arr_sum < x:
            return -1
        if arr_sum == x:
            return len(nums)
        
        required_subarray_sum = arr_sum - x
        left = curr_sum = max_subarray_size = 0
        
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > required_subarray_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == required_subarray_sum:
                max_subarray_size = max(max_subarray_size, right - left + 1)
                
        return len(nums) - max_subarray_size if max_subarray_size > 0 else -1
