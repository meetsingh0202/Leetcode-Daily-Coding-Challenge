class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        remainder = columnNumber % 26
        qoutient = columnNumber // 26
        
        ans = chr(64 + remainder)
        
        s = ""
        while columnNumber>0:
            columnNumber -= 1
            s += chr(columnNumber%26 + ord('A'))
            columnNumber //= 26
        s = s[::-1]
        return s
    