class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        currRange = []
        flag = False
        lastNum = -1
        
        for i in range(len(nums)):
            
            currNum = nums[i]
            
            if flag == False:
                currRange.append([currNum, 's'])
                flag = True
                lastNum = currNum
            
            else:
                if currNum == lastNum + 1:
                    if len(currRange) == 1:
                        currRange.append([currNum, 'e'])
                    else:
                        currRange[-1][0] = currNum
                    lastNum = currNum
                else:
                    if len(currRange) > 1:
                        res.append(str(currRange[0][0]) + '->' + str(currRange[1][0]))
                    else:
                        res.append(str(currRange[0][0]))
                    currRange = []
                    currRange.append([currNum, 's'])
                    lastNum = currNum
                    
            # print(res, currRange, currNum)
            
        if currRange:
            if len(currRange) > 1:
                res.append(str(currRange[0][0]) + '->' + str(currRange[1][0]))
            else:
                res.append(str(currRange[0][0]))
        
        return res