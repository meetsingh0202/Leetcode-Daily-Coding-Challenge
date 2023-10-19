class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack = []
        
        for i in range(len(s)):
            
            currChar = s[i]
            
            if currChar != '#':
                stack.append(currChar)
            else:
                if stack:
                    stack.pop()
        
        a = "".join(stack)
        
        stack = []
        
        for i in range(len(t)):
            
            currChar = t[i]
            
            if currChar != '#':
                stack.append(currChar)
            else:
                if stack:
                    stack.pop()
        
        b = "".join(stack)
        
        return a == b