class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        flights = defaultdict(list)
        
        tickets.sort()
        
        for i in tickets:
            x, y = i
            flights[x].append(y)
                
        res = ["JFK"]
        
        def traverse(curr):
            if len(res) == len(tickets) + 1:
                return True
            
            if curr not in flights:
                return False
            
            for index, val in enumerate(flights[curr]):
                flights[curr].pop(index)
                res.append(val)
                
                if traverse(val):
                    return True
                else:
                    flights[curr].insert(index, val)
                    res.pop()
            
            return False
            
        traverse("JFK")
        
        return res