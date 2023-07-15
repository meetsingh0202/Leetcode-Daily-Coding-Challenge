class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = []
        for i in range(n):
            starts.append(events[i][0])

        memo = {}
        def helper(i, k):
            if k == 0 or i == n:
                return 0
            
            if (i, k) in memo:
                return memo[(i, k)]
            
            next_ = bisect_right(starts, events[i][1])
            
            memo[(i, k)] = max(helper(i + 1, k), events[i][2] + helper(next_, k - 1))
            
            return memo[(i, k)]
        
        return helper(0, k)
