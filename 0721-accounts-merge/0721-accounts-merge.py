class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def union(x, y):
            # print('-----------')
            # print(p)
            # print(x, y)
            
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
    
    """
    [["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]
    [["David","David0@m.co","David5@m.co","David0@m.co"],["Lily","Lily4@m.co","Lily2@m.co","Lily0@m.co"],["Fern","Fern5@m.co","Fern2@m.co","Fern6@m.co"],["Gabe","Gabe0@m.co","Gabe6@m.co","Gabe8@m.co"],["Alex","Alex7@m.co","Alex5@m.co","Alex7@m.co"],["Lily","Lily4@m.co","Lily6@m.co","Lily7@m.co"],["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],["John","John4@m.co","John2@m.co","John0@m.co"]]
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
[["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
    
    """
    
    