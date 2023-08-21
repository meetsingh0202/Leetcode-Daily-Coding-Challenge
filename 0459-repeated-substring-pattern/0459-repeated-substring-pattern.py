class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        for i in range(len_s//2):
            substring =s[:i+1]
            if substring*(len_s//len(substring)) == s:
                return True
        return False