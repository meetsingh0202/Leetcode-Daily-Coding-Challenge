class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for i in asteroids:
            # print(stack, i)
            if i < 0:
                flag = 0
                while stack and stack[-1] > 0:
                    flag = 1
                    prev = stack[-1]
                    curr = i
                    
                    if prev < -1 * curr:
                        stack.pop()
                        flag = 0
                    
                    elif prev == -1 * curr:
                        stack.pop()
                        break
                        
                    else:
                        break
                if flag == 0:
                    stack.append(i)
            else:
                stack.append(i)
            
        return stack