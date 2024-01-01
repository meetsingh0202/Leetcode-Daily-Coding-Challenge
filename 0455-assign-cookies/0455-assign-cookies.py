class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        g.sort()
        s.sort()
        for j in range(len(s)):
            if i >= len(g):
                break
            if(s[j] >= g[i]):
                i += 1
        return i