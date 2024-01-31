class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            
            currElement = temperatures[i]
            currAns = 0
            
            while stack and stack[-1][0] <= currElement:
                stack.pop()
                
            if stack:
                currAns = (stack[-1][1] - i)
            
            stack.append([currElement, i])
            
            res.append(currAns)
        
        return res[ : : -1]