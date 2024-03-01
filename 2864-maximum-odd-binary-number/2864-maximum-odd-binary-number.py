class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = ['0'] * len(s)
        j = 0

        for i in range(len(s)):
            if s[i] == '1':
                ans[j] = '1'
                j += 1

        ans[j - 1], ans[-1] = ans[-1], '1'

        return ''.join(ans)
