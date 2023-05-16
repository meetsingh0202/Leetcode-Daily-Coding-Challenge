class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def union(x, y):
            pX, pY = find(x), find(y)
            if pY in total:
                p[pX] = pY
                p[x] = pY
                total[pY].add(x)
            else:
                p[pY] = p[pX]
                p[y] = pX
                total[pX].add(y)
            
        def find(x):
            if x not in p:
                p[x] = x
                return p[x]
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        res = []
        p = dict()
        total = defaultdict(set)
        
        adjacencyList = defaultdict(list)
        ownerName = dict()
        
        for i in accounts:
            name = i[0]
            if len(i) > 2:
                currEmail = i[1]
                ownerName[currEmail] = name
                for index in range(2, len(i)):
                    nextEmail = i[index]
                    if nextEmail == currEmail:
                        continue
                    ownerName[nextEmail] = name
                    if find(currEmail) != find(nextEmail):
                        if nextEmail in total:
                            union(nextEmail, currEmail)
                        else:
                            union(currEmail, nextEmail)
            else:
                ownerName[i[1]] = name
                union(i[1], i[1])
                
        count = set()
        res = []
        HashMap = defaultdict(set)
        
        for key, val in p.items():
            HashMap[find(val)].add(key)
        
        for key, val in HashMap.items():
            name = ownerName[key]
            val.add(key)
            tempList = list(val)
            res.append([name] + sorted(tempList))
        return res
    