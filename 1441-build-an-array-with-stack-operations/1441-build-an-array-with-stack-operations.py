class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        prev = -1
        targetIndex = 0
        lastGood = -1
        stackIndex = 0
        res = []
        stack = []
        
        for i in range(1, 101):
            if stack == target:
                return res
            
            while stack and stack[-1] < i and stack[-1] != lastGood:
                res.append("Pop")
                stack.pop()
                
            stack.append(i)
            res.append("Push")
            if stack[-1] == target[targetIndex]:
                lastGood = stack[-1]
                targetIndex += 1
                
        return res