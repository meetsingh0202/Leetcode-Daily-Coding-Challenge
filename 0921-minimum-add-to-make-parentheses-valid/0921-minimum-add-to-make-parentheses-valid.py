class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        countopened=0
        countclosed=0
        stack=[]
        for i in s:
            if stack and stack[-1]=='(' and i==')':
                stack.pop()
            else:
                stack.append(i)
        return (len(stack))