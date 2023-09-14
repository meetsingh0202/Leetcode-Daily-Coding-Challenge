from sortedcontainers import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        flights = dict()
        
        for i in tickets:
            x, y = i
            
            if x in flights:
                flights[x].add(y)
            else:
                flights[x] = SortedList()
                flights[x].add(y)
                
        res = ["JFK"]
        print(flights)
        
        def traverse(curr):
            if len(res) == len(tickets) + 1:
                return True
            
            if curr not in flights:
                return False
            
            for k in flights[curr]:
                flights[curr].remove(k)
                res.append(k)
                
                if traverse(k):
                    return True
                else:
                    flights[curr].add(k)
                    res.pop()
            
            return False
            
        traverse("JFK")
        
        return res