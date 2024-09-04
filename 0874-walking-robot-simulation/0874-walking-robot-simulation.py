class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        y = 0
        x = 0
        
        degrees_faced = 90
        max_dist = 0
        obstacles = set((i,j) for (i,j) in obstacles)
        
        
        for c in commands:
            degrees_faced = degrees_faced % 360
            if c == -2:
                degrees_faced += 90
            if c== -1:
                degrees_faced -= 90
            else:
                direction = []
                if degrees_faced  == 90:
                    direction = [0,1]
                elif degrees_faced == 180:
                    direction = [-1,0]
                elif degrees_faced == 270:
                    direction = [0,-1]
                elif degrees_faced  == 0:
                    direction = [1,0]
                    
                for i in range(c):
                    dx, dy = direction[0], direction[1]
                    if (x + dx, y + dy) in obstacles:
                        break
                    x+=dx
                    y+=dy
                
                dist = int(((x**2) + (y**2)))
                max_dist = max(max_dist, dist)
                
        return max_dist
