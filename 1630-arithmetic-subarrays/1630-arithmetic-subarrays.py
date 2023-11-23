class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(start, end):
            temp = nums[start : end + 1]            
            temp.sort()
            
            diff = temp[1] - temp[0]
            prevIndex = 1
            
            for i in range(2, len(temp)):
                tempDiff = temp[i] - temp[prevIndex]
                
                if tempDiff != diff:
                    return False
                
                prevIndex = i
            
            return True
                
        res = []
        
        for i in range(len(l)):
            x, y = l[i], r[i]
            
            if check(x, y):
                res.append(True)
            else:
                res.append(False)
        
        return res