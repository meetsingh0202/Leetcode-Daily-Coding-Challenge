class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def processLineWithOneWord(currLine, currLen, maxWidth):
            spaces = maxWidth - currLen
            resStr = currLine[0]
            
            while spaces > 0:
                resStr += " "
                spaces -=1
            
            res.append(resStr)
            
        def processLineWithKWord(currLine, currLen, maxWidth):
            
            spaces = maxWidth - currLen
            evenlySpaces = spaces // (len(currLine) - 1)
            unEvenSpaces = spaces % (len(currLine) - 1)
            
            i = 0
            
            while i < len(currLine) - 1:
                tempStr = currLine[i]
                k = 0
                while k < evenlySpaces:
                    tempStr += " "
                    k += 1
                
                currLine[i] = tempStr
                i += 1
            
            i = 0
            while unEvenSpaces > 0:
                tempStr = currLine[i]
                tempStr += " "
                currLine[i] = tempStr
                i += 1
                unEvenSpaces -= 1
            
            resStr = ""
            for i in range(len(currLine)):
                if i == 0:
                    resStr += currLine[i]
                else:
                    resStr += " " + currLine[i]
            
            res.append(resStr)
            
        def processLastLine(currLine, currLen, maxWidth):
            spaces = maxWidth - currLen
            
            resStr = ""
            
            for i in range(len(currLine)):
                if i == 0:
                    resStr += currLine[i]
                else:
                    resStr += " " + currLine[i]
        
            while spaces > 0:
                resStr += " "
                spaces -= 1
                
            res.append(resStr)
                
        res = []
        currLine = []
        currLine.append(words[0])
        
        currLen = len(words[0])
        
        for i in range(1, len(words)):
            
            if (currLen + len(words[i]) + 1 <= maxWidth):
                currLine.append(words[i])
                currLen += len(words[i]) + 1
            else:
                if (len(currLine) == 1):
                    processLineWithOneWord(currLine, currLen, maxWidth)
                else:
                    processLineWithKWord(currLine, currLen, maxWidth)
                    
                currLine = []
                currLine.append(words[i])
                currLen = len(words[i])
        
        processLastLine(currLine, currLen, maxWidth)
        
        return res