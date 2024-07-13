class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        stack = []
        
        robots = []
        
        for i in range(len(positions)):
            currPosition, currHealth, currDirection = positions[i], healths[i], directions[i]
            robots.append([currPosition, currHealth, currDirection, i + 1])
            
        robots.sort()
        
        
        for robot in robots:
            currPosition, currHealth, currDirection, currRobotNumber = robot
            
            flag = True
            
            while stack and stack[-1][2] == 'R' and currDirection == 'L':
                tempPosition, tempHealth, tempDirection, tempRobotNumber = stack.pop()
                
                if tempHealth < currHealth:
                    currHealth -= 1
                elif tempHealth > currHealth:
                    tempHealth -= 1
                    flag = False
                    stack.append([tempPosition, tempHealth, tempDirection, tempRobotNumber])
                    break
                else:
                    flag = False
                    break
                    
            if flag:
                stack.append([currPosition, currHealth, currDirection, currRobotNumber])
                
            # print(stack)
        
        res = []
        stack.sort(key = lambda x : x[3])
        
        for i in stack:
            res.append(i[1])
        
        return res