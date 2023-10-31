class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        def convert(curr, target):
            
            tempVal = 0
            
            for i in range(31, -1, -1):
                
                if curr & (1 << i):
                    x = 1
                else:
                    x = 0
                    
                if target & (1 << i):
                    y = 1
                else:
                    y = 0
                
                if x == 1 and y == 1:
                    tempVal = tempVal & ~(1 << i)
                    
                elif x == 1 and y == 0:
                    tempVal = tempVal | (1 << i)            
                    
                elif x == 0 and y == 0:
                    tempVal = tempVal & ~(1 << i)
                    
                elif x == 0 and y == 1:
                    tempVal = tempVal | (1 << i)
                
            return tempVal
        
#         1 0 1
#         0 1 0 
        
#         1 0 1
#         1 1 1
        
        arr = [pref[0]]
        currXor = pref[0]
        
        for i in pref[1:]:
            tempAns = convert(currXor, i)
            # print(i, tempAns, currXor)
            currXor = currXor ^ tempAns
            # print(i, tempAns, currXor)
            # break
            arr.append(tempAns)
        
        return arr