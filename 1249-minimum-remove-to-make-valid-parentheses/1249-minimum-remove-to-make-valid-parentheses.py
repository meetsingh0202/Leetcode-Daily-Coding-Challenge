class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        res = []
        tempIndex = 0
        
        for index, val in enumerate(s):
            
            if val == '(':
                stack.append(tempIndex)
                tempIndex += 1
                res.append('(')
                
            elif val == ')':
                if stack:
                    stack.pop()
                    res.append(')')
                    tempIndex += 1
                    
            else:
                res.append(val)
                tempIndex += 1
        
        if stack:
            for i in stack:
                res[i] = ''
                
        return "".join(res)