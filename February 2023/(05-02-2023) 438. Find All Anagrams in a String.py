class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        lenofwindow=len(p)
        if lenofwindow>len(s):
            return []
        
        HashMapofS = dict()
        HashMapofP = dict()
        for i in range(len(p)):
            HashMapofP[p[i]] = 1 + HashMapofP.get(p[i], 0)
            HashMapofS[s[i]] = 1 + HashMapofS.get(s[i], 0)
            
        res = []
        if (HashMapofP==HashMapofS):
            res.append(0)
            
        left = 0
        for right in range(len(p), len(s)):
            currChar = s[right]
            HashMapofS[currChar] = 1 + HashMapofS.get(currChar,0)
            HashMapofS[s[left]] -= 1
            if HashMapofS[s[left]] == 0:
                del HashMapofS[s[left]]
            left+=1
            if HashMapofS == HashMapofP:
                res.append(left)
        return res
