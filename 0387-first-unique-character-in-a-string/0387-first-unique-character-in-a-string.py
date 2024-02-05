class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequecy = {}
        for i in range(len(s)):
            if s[i] not in frequecy:
                frequecy[s[i]] = 1
            else:
                frequecy[s[i]] = frequecy[s[i]] + 1
        for i in range(len(s)):
            if frequecy[s[i]]==1:
                return i
        return -1