class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLen, indices = -1, {}
        for i, c in enumerate(s):
            maxLen = max(maxLen, i - indices.setdefault(c, i + 1))
        return maxLen