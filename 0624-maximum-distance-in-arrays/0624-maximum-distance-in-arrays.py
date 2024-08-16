class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn, mx = arrays[0][0], arrays[0][-1]
        diff = -float("inf")
        for ar in arrays[1:]:
            mx_diff = abs(mx - ar[0])
            mn_diff = abs(mn - ar[-1])
            diff = max(diff, mn_diff, mx_diff)
            if ar[0] < mn:
                mn = ar[0]
            if ar[-1] > mx:
                mx = ar[-1]
        return diff
