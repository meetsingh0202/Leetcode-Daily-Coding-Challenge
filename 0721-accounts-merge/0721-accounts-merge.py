class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_graph[acc[1]].add(email)
                em_graph[email].add(acc[1])
                em_to_name[email] = name
    
        seen = set()
        ans = []
        for email in em_graph:
            if email not in seen:
                seen.add(email)
                q = [email]
                component = []
                while q:
                    edge = q.pop(0)
                    component.append(edge)
                    for nei in em_graph[edge]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans
#         def union(x, y):
#             print('-----------')
#             print(p)
#             print(x, y)
            
#             if p[y] != y:
#                 p[find(x)] = p[find(y)]
#                 total[find(y)].add(x)
#             else:
#                 p[find(y)] = p[find(x)]
#                 total[find(x)].add(y)
            
#         def find(x):
#             if x not in p:
#                 p[x] = x
#                 return p[x]
                
#             if x != p[x]:
#                 p[x] = find(p[x])
#             return p[x]
        
#         res = []
#         p = dict()
#         total = defaultdict(set)
        
#         adjacencyList = defaultdict(list)
#         ownerName = dict()
        
#         for i in accounts:
#             name = i[0]
#             if len(i) > 2:
#                 currEmail = i[1]
#                 ownerName[currEmail] = name
#                 for index in range(2, len(i)):
#                     nextEmail = i[index]
#                     ownerName[nextEmail] = name
#                     if find(currEmail) != find(nextEmail):
#                         union(currEmail, nextEmail)
#             else:
#                 ownerName[i[1]] = name
#                 union(i[1], i[1])
                
#         count = set()
#         res = []
        
#         for key, val in total.items():
#             temp = []
#             name = ownerName[key]
#             if len(val) > 0:
#                 val.add(key)
#                 temp.append(name)
#                 temp.extend(sorted(list(val)))
#             else:
#                 temp.append(name)
#                 temp.append(key)
#             res.append(temp)
#         return res
    