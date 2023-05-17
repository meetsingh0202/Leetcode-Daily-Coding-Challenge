#User function Template for python3

import sys
sys.setrecursionlimit(10**6)
from collections import *

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        
        def traverse(curr, parent):
            nonlocal parentCount, counter
            # print(curr, parent, disc, low)
            visited.add(curr)
            points = set()
    
            for index, i in enumerate(adj[curr]):
                if i != parent:
                    if i in visited:
                        points.add(i)
                    else:
                        if curr == src:
                            parentCount += 1
                        counter += 1
                        low[i] = counter
                        disc[i] = counter
                        traverse(i, curr)
                        points.add(i)
                        if curr != src and disc[curr] <= low[i]:
                            articulationPoints.add(curr)
    
            if len(points) > 0:
                for x in points:
                    low[curr] = min(low[curr], low[x])
    
    
        articulationPoints = set()
        visited = set()
        parentCount = 0
        counter = 0
        disc = dict()
        low = dict()
        k = 0
        src = k
        disc[k] = 0
        low[k] = 0
        traverse(k, -1)
        if parentCount > 1:
            articulationPoints.add(k)
            
        res = list(articulationPoints)
        res.sort()
        if len(res) > 0:
            return res
        return [-1]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends