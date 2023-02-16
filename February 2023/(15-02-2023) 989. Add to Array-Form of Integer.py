class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        currSum = 0 
        for i in range(len(num)):
            currSum += num[i]
            if i != len(num) - 1:
                currSum *= 10
        
        currSum += k
        
        res = []
        while currSum:
            currVal = currSum % 10
            res.append(currVal)
            currSum = currSum // 10
        
        return res[::-1]
