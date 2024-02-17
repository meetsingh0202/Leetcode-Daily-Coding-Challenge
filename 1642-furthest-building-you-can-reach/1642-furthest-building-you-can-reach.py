class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        count=0
        heap=[]
        for i in range(len(heights)-1):
            if heights[i]>=heights[i+1]:
                count+=1
                continue
            
            diff=heights[i+1]-heights[i]
            heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return i
            
        return len(heights)-1