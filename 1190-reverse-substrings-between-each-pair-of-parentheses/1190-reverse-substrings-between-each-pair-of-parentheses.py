class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char == ')':
                tempString = ""
                while stack and stack[-1] != '(':
                    tempString += stack.pop()
                stack.pop()
                stack.extend(tempString)
            else:
                stack.append(char)
        
        return "".join(stack)