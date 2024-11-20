class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        HashMap = dict()
        HashMap['a'] = 0
        HashMap['b'] = 0
        HashMap['c'] = 0
        Index = defaultdict(list)
        
        for index, i in enumerate(s):
            HashMap[i] = 1 + HashMap.get(i, 0)
        
        if HashMap['a'] < k:
            return -1
        if HashMap['b'] < k:
            return -1
        if HashMap['c'] < k:
            return -1
        
        n = len(s)
        res = len(s)
        left = 0
        
        for right in range(n):
            HashMap[s[right]] -= 1
            
            while left <= right and (HashMap['a'] < k or HashMap['b'] < k or HashMap['c'] < k):
                HashMap[s[left]] += 1
                left += 1
            res = min(res, HashMap['a'] + HashMap['b'] + HashMap['c'])
            
        return res
            