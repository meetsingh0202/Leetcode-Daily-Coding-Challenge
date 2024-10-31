class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        @cache
        def traverse(currRobot, currFactory, currRepair):
            if currRobot == len(robot):
                return 0
            if currFactory == len(factory):
                return float('inf')
            
            take = float('inf')
            notTake = float('inf')
            
            notTake = traverse(currRobot, currFactory + 1, 0)
            
            if currRepair < factory[currFactory][1]:
                take = abs(robot[currRobot] - factory[currFactory][0]) + traverse(currRobot + 1, currFactory, currRepair + 1) 
            
            return min(take, notTake)
            
        
        robot.sort()
        factory.sort()
        return traverse(0, 0, 0)
            