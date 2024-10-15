class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        j = 0
        for i in range(len(s)):
            if(s[i] == '0'):
                ans += i - j
                j += 1
        return ans
