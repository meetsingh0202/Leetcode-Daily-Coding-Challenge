class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
#         x1, y1 = coordinates[0]
#         x2, y2 = coordinates[1]
#         try:
#             lastSlope = (y2 - y1) // (x2 - x1)
#         except:
#             lastSlope = 0
            
#         for i in range(1, len(coordinates) - 1):
#             x1, y1 = coordinates[i]
#             x2, y2 = coordinates[i + 1]
#             try:
#                 currSlope = (y2 - y1) // (x2 - x1)
#             except:
#                 currSlope = 0
            
#             if currSlope != lastSlope:
#                 return False
            
#         return True
    
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
                return False

        return True