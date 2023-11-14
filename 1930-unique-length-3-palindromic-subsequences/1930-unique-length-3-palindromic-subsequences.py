class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}

        for index,c in enumerate(s):
            if c not in first:
                first[c]= index
            last[c] = index

        total = 0
        for c in string.ascii_lowercase:
            if c not in first:
                continue

            seen = set()
            for i in range(first[c] +1, last[c]):
                seen.add(s[i])
            total += len(seen)
        return total