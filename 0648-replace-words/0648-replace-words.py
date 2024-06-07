class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        wordSet = set()
        
        for i in dictionary:
            wordSet.add(i)
            
        res = []
        
        for word in sentence.split(' '):
            
            currWord = ""
            flag = False
            
            for char in word:
                currWord += char
                # print(currWord)
                if currWord in wordSet:
                    res.append(currWord)
                    # print(res, currWord)
                    flag = True
                    break
            
            if flag == False:
                res.append(word)
                        
        return " ".join(res)
        