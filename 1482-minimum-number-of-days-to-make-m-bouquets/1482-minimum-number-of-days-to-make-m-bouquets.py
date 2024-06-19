class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(mid):
            count = 0
            currWait = 0
            i = 0
            currK = 0
            while i < len(bloomDay):
                if bloomDay[i] > mid:
                    i += 1
                    currK = 0
                    continue
                currK += 1
                if currK == k:
                    count += 1
                    currK = 0
                i += 1
            # print(count, mid)
            return count >= m
        
        low = 1
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) >> 1
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans