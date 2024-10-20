class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for chr in expression:
            if chr == ',':
                continue

            if chr in ['!', '&', '|', '(']:
                stack.append(chr)

            elif chr == ')':
                eval = []
                while stack[-1] != '(':
                    eval.append(stack.pop())
                
                stack.pop()
                op = stack.pop()
                if op == '&':
                    stack.append(all(eval))
                elif op == "|":
                    stack.append(any(eval))
                else:
                    stack.append(not eval[0])

            elif chr == 't':
                stack.append(1)
            
            else:
                stack.append(0)

        return stack[0]