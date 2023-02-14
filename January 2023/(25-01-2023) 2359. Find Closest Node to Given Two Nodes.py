class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def traverse(Node, currDistance, dist):
            if dist[Node] != -1:
                return
            dist[Node] = currDistance
            
            nextNode = edges[Node]
            if nextNode != -1:
                traverse(nextNode, currDistance + 1, dist)
                    
        dist1 = [-1] * len(edges)
        dist2 = [-1] * len(edges)
        traverse(node1, 0, dist1)
        traverse(node2, 0, dist2)
        
        Min = float('inf')
        minimumNode = -1
        for i in range(len(edges)): 
            currDistance1, currDistance2 = dist1[i], dist2[i]
            if currDistance1 != -1 and currDistance2 != -1:
                currDistance = max(currDistance1, currDistance2)
                
                if Min > currDistance:
                    Min = currDistance
                    minimumNode = i
                    
        return minimumNode
