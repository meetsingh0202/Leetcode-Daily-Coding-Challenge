class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        lastIndex = dict()
        totalCount = 0
        
        for i in range(len(garbage)):
            currHouse = garbage[i]
            
            if 'P' in currHouse:
                lastIndex['P'] = i
            
            if 'G' in currHouse:
                lastIndex['G'] = i
            
            if 'M' in currHouse:
                lastIndex['M'] = i
                
            totalCount += len(currHouse)
        
        prefixSum = [0, travel[0]]
        
        for i in travel[1:]:
            prefixSum.append(prefixSum[-1] + i)
        
        # print(lastIndex)
        # print(prefixSum)
        # print(totalCount)
        
        for i in "PGM":
            if i in lastIndex:
                totalCount += prefixSum[lastIndex[i]]
        
        return totalCount