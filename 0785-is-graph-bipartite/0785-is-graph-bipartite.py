
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        queue = deque()
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    for nb in graph[node]:
                        if nb in color:
                            if color[nb] == color[node]:
                                return False
                        else:
                            color[nb] = 1 - color[node]
                            queue.append(nb)
        return True