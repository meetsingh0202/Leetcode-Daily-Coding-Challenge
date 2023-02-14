class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return []
        
        def isValid(s):
            if len(s) > 1 and int(s[0]) == 0:
                return False
            if len(s) > 3 or int(s) > 255:
                return False
            return True
        
        def backtrack(i,dots,curr):
            if dots==4 and i==len(s):
                res.append(curr[:-1])
                return
            for j in range(i,min(i+3,len(s))):
                temp=s[i:j+1]
                if isValid(temp):
                    backtrack(j+1,dots+1,curr+str(temp)+'.')

        backtrack(0,0,"")
        return res
