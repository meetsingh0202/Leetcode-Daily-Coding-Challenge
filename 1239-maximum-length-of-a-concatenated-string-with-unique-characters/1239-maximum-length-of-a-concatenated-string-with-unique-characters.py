class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        @cache
        def traverse(currIndex, currChars):
            
            if currIndex == len(arr):
                return 0
            
            tempString = arr[currIndex]
            
            take, notTake = float('-inf'), float('-inf')
            flag = True
            tempMask = currChars
            
            for char in tempString:
                tempIndex = ord(char) - ord('a')
                
                if tempMask & (1 << tempIndex):
                    flag = False
                    break
                
                tempMask = tempMask | (1 << tempIndex)
            
            if flag:
                take = len(tempString) + traverse(currIndex + 1, tempMask)
            
            notTake = traverse(currIndex + 1, currChars)
            
            return max(take, notTake)
        
        return traverse(0, 0)
    