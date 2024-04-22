class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        choices = defaultdict(list)
        
        for i in range(10):
            choices[i].append((i + 1) % 10)
        
        for key, val in choices.items():
            choices[val[0]].append(key)
        deadends = set(deadends)
        
        q = deque(['0000'])
        visited = set()
        time = 0
        while q:
            for _ in range(len(q)):
                tempVal = q.popleft()
                if tempVal == target:
                    return time
                if tempVal in deadends:
                    continue
                for i in range(len(tempVal)):
                    for j in choices[int(tempVal[i])]:
                        tempVal1 = tempVal[:i] + str(j) + tempVal[i + 1:]
                        if tempVal1 not in visited:
                            q.append(tempVal1)
                            visited.add(tempVal1)
            time += 1
        return -1