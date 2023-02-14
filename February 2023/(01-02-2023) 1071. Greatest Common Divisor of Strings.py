class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def check(currString):
            lenofcurrString = len(currString)
            multiplesfor1 = lenofstr1 // lenofcurrString
            multiplesfor2 = lenofstr2 // lenofcurrString
            
            tempStr1 = multiplesfor1 * currString
            tempStr2 = multiplesfor2 * currString
            if tempStr1 == str1 and tempStr2 == str2:
                return True
            return False
            
        prefixes = set()
        lenofstr1 = len(str1)
        lenofstr2 = len(str2)
        
        for i in range(len(str1) + 1):
            currString = str1[:i]
            prefixes.add(currString)
        
        for i in range(len(str2) + 1):
            currString = str2[:i]
            prefixes.add(currString)
        prefixes = list(prefixes)
        prefixes.sort(key = len, reverse = True)
        prefixes = prefixes[: -1]
        # print(prefixes)
        for i in prefixes:
            if check(i):
                return i
        return ""
