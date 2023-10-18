class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        dependentBy = defaultdict(list)
        dependentOn = defaultdict(list)
        
        for i in relations:
            x, y = i
            
            dependentOn[y].append(x)
            dependentBy[x].append(y)
            
        queue = deque([])
        
        cost = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if i not in dependentOn:
                queue.append(i)
                cost[i] = time[i - 1]
        
        total = 0
        while queue:
            # print(queue)
            for i in range(len(queue)):
                
                currNode = queue.popleft()
                
                for i in dependentBy[currNode]:
                    dependentOn[i].remove(currNode)
                    cost[i] = max(cost[i], time[i - 1] + cost[currNode])
                    
                    if len(dependentOn[i]) == 0:
                        del dependentOn[i]
                        queue.append(i)
                        
            # print(cost)
        
        return max(cost)