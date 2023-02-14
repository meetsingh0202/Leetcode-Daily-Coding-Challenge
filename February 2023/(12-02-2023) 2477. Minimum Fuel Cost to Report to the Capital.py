class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacencyList = defaultdict(list)
        
        for i in roads:
            x, y = i
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        q = deque([0])
        
        visited = set()
        leafCity = deque([])
        while q:
            currCity = q.popleft()
            flag = 0
            visited.add(currCity)
            for i in adjacencyList[currCity]:
                if i not in visited:
                    flag = 1
                    q.append(i)
            if flag == 0:
                leafCity.append(currCity)
                
        q = deque([])
        for i in leafCity:
            q.append([i, 0, seats - 1])
            
        totalCost = 0
        visited = set()
        
        while q:
            currCity, currLitres, currSeats = q.popleft()
                
            if currCity == 0:
                totalCost += currLitres
                continue
            
            visited.add(currCity)   
            flag = 0
            for i in adjacencyList[currCity]:
                if i not in visited:
                    flag = 1
                    if currSeats > 0:
                        q.append([i, currLitres + 1, currSeats - 1])
                    else:
                        if i != 0:
                            q.append([i, currLitres + 1, 0])
                            q.append([i, 0, seats - 1])
                        else:
                            q.append([i, currLitres + 1, 0])
        return totalCost
            
            
