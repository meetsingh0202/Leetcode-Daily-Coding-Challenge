class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def traverse(src, des):
            distance = [float('inf')] * n
            distance[src] = 0

            minHeap = [(0, src)]
        
            while minHeap:
                cost, curr = heappop(minHeap)

                if cost > distance[curr]:
                    continue

                for neigh, neigh_cost in adj[curr]:
                    new_cost = cost + neigh_cost
                    
                    if new_cost < distance[neigh]:
                        distance[neigh] = new_cost
                        heappush(minHeap, (new_cost, neigh))

            return distance[des]

        MaxVal = 2 * 10**9

        adj = defaultdict(list)
        for src, des, w in edges:
            if w != -1:
                adj[src] += [(des, w)]
                adj[des] += [(src, w)]

        initialDistance = traverse(source, destination)

        if initialDistance < target:
            return []

        if initialDistance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = MaxVal

            return edges

        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                edges[i][2] = 1
                adj[u] += [(v, 1)]
                adj[v] += [(u, 1)]

                tempDistance = traverse(source, destination)

                
                if tempDistance <= target:
                    diff = target - tempDistance
                    edges[i][2] += diff

                    for j in range(i + 1, len(edges)):
                        if edges[j][2] == -1:
                            edges[j][2] = MaxVal

                    return edges
            
        return []