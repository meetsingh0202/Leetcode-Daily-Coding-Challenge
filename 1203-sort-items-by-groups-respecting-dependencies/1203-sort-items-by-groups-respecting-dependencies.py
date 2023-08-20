class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(graph,indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]

            while stack:
                curr = stack.pop()
                visited.append(curr)
                for conn in graph[curr]:
                    indegree[conn]-=1
                    if indegree[conn] == 0:
                        stack.append(conn)
            return visited if len(visited) == len(graph) else []
        
        ans=[]
        inDegree=[0]*n
        itemGraph=[[] for _ in range(n)]

        unique_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = unique_group_id
                unique_group_id += 1
        
        group_inDegree=[0]*unique_group_id
        groupGraph=[[] for _ in range(unique_group_id)]

        for i in range(n):
            for before in beforeItems[i]:
                itemGraph[before].append(i)
                inDegree[i]+=1
            
                if group[i] != group[before]:
                    groupGraph[group[before]].append(group[i])
                    group_inDegree[group[i]]+=1
        
        o_item=topologicalSort(itemGraph,inDegree)
        o_group=topologicalSort(groupGraph,group_inDegree)

        if not o_item or not o_group:
            return []
        
        o_itemByGroup=defaultdict(list)
        for i in o_item:
            o_itemByGroup[group[i]].append(i)
        
        for g in o_group:
            ans+=o_itemByGroup[g]
        
        return ans