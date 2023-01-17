class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        smallest = dict()
        
        for i in string.ascii_lowercase:
            smallest[i] = i
        
        def getSmallest(x):
            if smallest[x] != x:
                smallest[x] = getSmallest(smallest[x])
            return smallest[x]
        
        for a, b in zip(s1, s2):
            smaller = min(getSmallest(a), getSmallest(b))
            
            smallest[getSmallest(a)] = smaller
            smallest[getSmallest(b)] = smaller
            
        ans = []
        for i in baseStr:
            ans.append(getSmallest(i))
        
        return "".join(ans)
