class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        print(s)
        word = s.split(" ")
        print(word)
        return len(word[-1])