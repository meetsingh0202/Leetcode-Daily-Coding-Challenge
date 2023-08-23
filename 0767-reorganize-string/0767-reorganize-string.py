class Solution:
    def reorganizeString(self, s: str) -> str:
        
        HashMap = dict()
        
        for i in s:
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        HashMap = sorted(HashMap.items(), key = lambda x : x[1], reverse = True)
            
        for i in range(len(HashMap)):
            temp = [-HashMap[i][1], HashMap[i][0]]
            HashMap[i] = temp
            
        finalStr = ""
        prevChar = ""
        while HashMap:
            currVal, currChar = heappop(HashMap)
            currVal = -currVal
            if prevChar == currChar:
                l = [-currVal, currChar]
                if len(HashMap) > 0:
                    currVal, currChar = heappop(HashMap)
                    currVal = - currVal
                else:
                    return ""
                heappush(HashMap, l)
            finalStr += currChar
            currVal -=1 
            if currVal > 0:
                heappush(HashMap, [-currVal, currChar])
            prevChar = currChar
            # print(finalStr, HashMap)
        return finalStr
            
        
            