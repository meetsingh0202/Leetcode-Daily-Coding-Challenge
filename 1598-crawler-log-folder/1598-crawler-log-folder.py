class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i, e in enumerate(logs):
            if e =="./":
                continue
            elif e == "../":
                if ans == 0:
                    continue
                ans -= 1
            else:
                ans+=1
        return ans
