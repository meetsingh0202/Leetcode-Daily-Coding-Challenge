class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total_flips, cnt_flips, pref_sum = 0, 0, [0]*(len(nums)+1)
        for i in range(len(nums)):
            cnt_flips -= pref_sum[i]
            if nums[i] == cnt_flips%2:
                if i > len(nums)-k:
                    return -1
                cnt_flips += 1
                pref_sum[i+k] = 1
                total_flips += 1
        return total_flips
