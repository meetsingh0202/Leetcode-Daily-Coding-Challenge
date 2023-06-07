class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        heap = []
        
        for i in range(len(dist)):
            d, s, t = dist[i], speed[i], math.ceil(dist[i] / speed[i])
            heappush(heap, t)
        
        
        count = 0
        
        while heap:
            time = heappop(heap)
            
            if time - count <= 0:
                return count
            
            count += 1

        return count
            
            
            