class Solution:
    def sortVowels(self, s: str) -> str:
        
        
        vowels = []
        t = []
        
        for i in s:
            if i in "AEIOUaeiou":
                vowels.append(i)
        
        vowels.sort()
        index = 0
        
        for i in s:
            if i in "AEIOUaeiou":
                t.append(vowels[index])
                index += 1
            else:
                t.append(i)
                
        return "".join(t)