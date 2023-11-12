class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        HashMap = defaultdict(set)
        
        for index, val in enumerate(routes):
            for eachStop in val:
                HashMap[eachStop].add(index)
                
        q = deque([source])
        
        visitedIndex = set()
        visitedStop = set()
        ans = 0
        
        while q:
            for i in range(len(q)):
                currStation = q.popleft()
                if currStation == target:
                    return ans
                
                for i in HashMap[currStation]:
                    if i not in visitedIndex:
                        for k in routes[i]:
                            if k not in visitedStop:
                                q.append(k)
                                visitedStop.add(k)
                        visitedIndex.add(i)

            ans += 1
        return -1