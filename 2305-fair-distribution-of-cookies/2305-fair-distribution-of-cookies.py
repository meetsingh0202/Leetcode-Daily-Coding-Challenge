class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        @cache
        def dfs(i, dist):
            if i == len(cookies):
                return max(dist)
            new_dist = list(dist)
            ans = float("inf")
            for j in range(k):
                new_dist[j] += cookies[i]
                ans = min(ans, dfs(i+1, tuple(sorted(new_dist))))
                new_dist[j] -= cookies[i]
            return ans
        return dfs(0, (0, )*k)
