class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def checkSequence(num):
            for i in range(len(num) - 1):
                if int(num[i]) + 1 != int(num[i + 1]):
                    return False
            return True
        
        def getNext(num):
            tempNum = str(num)
            currFirstDigit = int(tempNum[0])
            str1 = str(currFirstDigit + 1)
            currFirstDigit += 1
            for i in range(1, len(tempNum)):
                currFirstDigit += 1
                str1 += str(currFirstDigit)
            
            if len(str1) > len(tempNum):
                temp = '1' + ('0' * len(tempNum))
                return getNext1(int(temp))    
            
            return str1
        
        def getNext1(num):
            tempNum = str(num)
            currFirstDigit = int(tempNum[0])
            str1 = tempNum[0]
            for i in range(1, len(tempNum)):
                currFirstDigit += 1
                str1 += str(currFirstDigit)
            return str1
            
        curr = low
        res = []
        k = 2
        while k:
            if curr > high:
                return res
            if res and res[-1] == curr:
                tempNext = getNext(curr)
            elif curr == low:
                tempNext = getNext1(curr)
                if checkSequence(tempNext) == False:
                    tempNext = getNext(curr)
            else:
                tempNext = getNext(curr)
            curr = int(tempNext)
            if checkSequence(tempNext) and (low <= curr <= high):
                res.append(curr)