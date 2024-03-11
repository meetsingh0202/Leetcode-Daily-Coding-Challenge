class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt, ans = Counter(T), ""
        for s in S:
            if s in cnt:
                ans += s*cnt[s]
                cnt.pop(s)
                
        return ans + "".join(s*cnt[s] for s in cnt) 