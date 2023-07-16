class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        def traverse(currIndex, currMask):
            if currMask == reqMask:
                return 0
            
            if currIndex == len(maskArr):
                return float('inf')
            
            if (currIndex, currMask) in memo:
                return memo[(currIndex, currMask)]
            
            take = 1 + traverse(currIndex + 1, currMask | maskArr[currIndex])
            notTake = traverse(currIndex + 1, currMask)
            
            if take < notTake:
                hasChoosen[(currIndex, currMask)] = True
                
            memo[(currIndex, currMask)] = min(take, notTake)
            return memo[(currIndex, currMask)]
        
        skillIndex = dict()
        
        for index, skill in enumerate(req_skills):
            skillIndex[skill] = index
        
        maskArr = []
        
        for person in people:
            temp = 0
            for personSkill in person:
                temp |= 1 << skillIndex[personSkill]
                
            maskArr.append(temp)
        
        reqMask = (1 << len(req_skills)) - 1
        
        memo = dict()
        hasChoosen = dict()
        
        traverse(0, 0)
        
        res = []
        tempMask = 0
        
        for i in range(len(maskArr)):
            if (i, tempMask) in hasChoosen:
                res.append(i)
                tempMask |= maskArr[i]
                
            if tempMask == reqMask:
                break
                
        return res