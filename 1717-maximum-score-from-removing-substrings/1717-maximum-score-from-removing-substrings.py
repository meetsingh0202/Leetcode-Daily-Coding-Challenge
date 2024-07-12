class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        count = 0
        
        if x > y:
            score1 = x
            score2 = y
            substring1 = "ab"
            substring2 = "ba"
        else:
            score1 = y
            score2 = x
            substring1 = "ba"
            substring2 = "ab"
        
        stack1, stack2 = [], []
        
        for char in s:
            if char == substring1[1] and stack1 and stack1[-1] == substring1[0]:
                stack1.pop()
                count += score1
            else:
                stack1.append(char)
        
        
        newString = "".join(stack1)
        
        for char in newString:
            if char == substring2[1] and stack2 and stack2[-1] == substring2[0]:
                stack2.pop()
                count += score2
            else:
                stack2.append(char)
        
        return count