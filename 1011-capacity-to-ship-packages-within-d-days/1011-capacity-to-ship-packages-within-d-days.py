class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def check(mid):
            currDays = 1
            currSum = 0
            
            for i in weights:
                if currSum + i <= mid:
                    currSum += i
                else:
                    currDays += 1
                    if currDays > days or i > mid:
                        return False
                    currSum = i
            
            return True
        
        low = max(weights)
        high = sum(weights)
        ans = high
        
        while low <= high:
            mid = (low + high) >> 1
            
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans