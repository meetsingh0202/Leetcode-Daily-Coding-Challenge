class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def traverse(currStr, currRes):
            for i in range(len(currStr) + 1):
                prefix = currStr[:i]
                suffix  = currStr[i:]
                if prefix in HashSet:
                    traverse(suffix, currRes + [prefix])
            res.append(currRes)
            
        HashSet = set()
        for word in wordDict:
            HashSet.add(word)
        
        res = []    
        traverse(s, [])
        
        finalres = []
        
        for i in res:
            currSum = 0
            currStr = ""
            for j in i:
                currSum += len(j)
                currStr += j
                currStr += ' '
            if currSum == len(s):
                currStr = currStr[:-1]
                finalres.append(currStr)
            
        return finalres