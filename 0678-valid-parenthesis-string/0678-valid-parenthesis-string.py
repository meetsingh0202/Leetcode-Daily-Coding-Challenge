class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def traverse(currIndex, count):
            
            if (currIndex, count) in memo:
                return memo[(currIndex, count)]
            
            if currIndex >= len(s):
                return count == 0

            if count < 0:
                return False

            if s[currIndex] == '(':
                return traverse(currIndex + 1, count + 1)

            if s[currIndex] == ')':
                if count == 0:
                    return False
                return traverse(currIndex + 1, count - 1)

            if s[currIndex] == '*':
                return traverse(currIndex + 1, count) or traverse(currIndex + 1, count + 1) or traverse(currIndex + 1, count - 1)

        memo = dict()
        return traverse(0, 0)