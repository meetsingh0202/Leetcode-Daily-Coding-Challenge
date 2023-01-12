class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        countOfApples = 0
        appleIndex = []
        for index in range(len(hasApple)):
            if hasApple[index] == True:
                countOfApples += 1
                appleIndex.append(index)
        
        adjacencyList = defaultdict(list)
        for i in edges:
            a, b = i
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        
        def traverse(currRoot, parent):
            currTime = 0
            for n in adjacencyList[currRoot]:
                if n != parent:
                    currTime += traverse(n, currRoot)
            if (currTime or hasApple[currRoot]) and currRoot != 0:
                currTime += 2
            return currTime
        
        totalStepCount = 0
        totalStepCount += traverse(0, -1)
        return totalStepCount
