class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        dict1={}
        l=0
        res=0
        
        for r in range(len(s)):
            dict1[s[r]] = 1 + dict1.get(s[r],0)
            # print(dict1)
            while (r - l + 1) - max(dict1.values()) > k:
                dict1[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res