class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(ord(s[idx-1]) - ord(s[idx])) for idx in range(1, len(s))])
