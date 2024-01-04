class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def findMul(num):
            a, b = 0, 0
            temp = float('inf')
            
            for i in range(num // 3 + 1):
                a = 3 * i
                remaining = num - a
                
                if remaining % 2 == 0:
                    temp = min(temp, i + remaining // 2)
            
            return temp
        
        HashMap = dict()
        count = 0
        
        for i in nums:
            HashMap[i] = 1 + HashMap.get(i, 0)
        print(HashMap)
        
        for key, val in HashMap.items():
            
            tempVal = findMul(val)  
            if tempVal == float('inf'):
                return -1 
            
            count += tempVal
            # print(findMul(val))
            
        return count