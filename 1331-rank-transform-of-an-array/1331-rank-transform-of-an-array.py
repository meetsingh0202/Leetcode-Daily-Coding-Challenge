class Solution:
    def arrayRankTransform(self, t: List[int]) -> List[int]:
        arr=sorted(list(set(t)))
        d={}
        num=1
        for a in arr:
            d[a]=num
            num+=1
        for a in range(len(t)):
            t[a]=d[t[a]]
        return t

