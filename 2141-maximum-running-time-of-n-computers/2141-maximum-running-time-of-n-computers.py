class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        ans = -1
        def helper(mid):
            time = 0
            for i in batteries:
                if i>=mid:
                    time+=mid
                else:
                    time+=i
            return time/n >=mid
        
        i, j = 0,10**15
        
        while i<j:
            mid = (i+j)//2
            if helper(mid):
                ans = mid
                i = mid+1
            else:
                j = mid
        return ans