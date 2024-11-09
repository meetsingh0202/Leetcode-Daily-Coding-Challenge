class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        count = 0
        word = list(word)
        
        for i in range(len(word)):
            
            currOrd = ord(word[i])
            flag = False
                        
            if i > 0:
                prevOrd = ord(word[i - 1])
                
                if abs(currOrd - prevOrd) <= 1:
                    flag = True
            
            if flag:
                word[i] = '@'
                count += 1
            
            # print(flag, i)
        
        return count