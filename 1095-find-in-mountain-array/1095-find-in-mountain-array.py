# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def getVal(self, index, mountain_arr):
        if index in self.memo:
            return self.memo[index]
        self.memo[index] = mountain_arr.get(index)
        return self.memo[index]

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def getPeakElement(n, mountain_arr):
            low = 0
            high = n - 1
            
            while low <= high:
                mid = (low + high) >> 1
                currVal = mountain_arr.get(mid)
                
                if mid + 1 < n:
                    nextVal = self.getVal(mid + 1, mountain_arr)
                else:
                    nextVal = float('-inf')
                    
                if mid - 1 >= 0:
                    prevVal = self.getVal(mid - 1, mountain_arr)
                else:
                    prevVal = float('-inf')
                    
                if currVal > nextVal and currVal > prevVal:
                    return mid
                
                if currVal < nextVal:
                    low = mid + 1
                
                elif currVal > nextVal:
                    high = mid - 1
        
        def findElementFirstParition(start, end, target):
            low = start
            high = end
            ans = -1
            
            while low <= high:
                mid = (low + high) >> 1
                
                currVal = self.getVal(mid, mountain_arr) 
                
                if currVal == target:
                    ans = mid
                    high = mid - 1
                
                elif currVal < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return ans
        
        def findElementSecondParition(start, end, target):
            low = start
            high = end
            ans = -1
            
            while low <= high:
                mid = (low + high) >> 1
                currVal = self.getVal(mid, mountain_arr) 
                
                if currVal == target:
                    ans = mid
                    low = mid + 1
                
                elif currVal < target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans
                
        self.memo = dict()  
        n = mountain_arr.length()
        peakElementIndex = getPeakElement(n, mountain_arr)
        
        if self.getVal(peakElementIndex, mountain_arr) == target:
            return peakElementIndex
        
        partition1 = findElementFirstParition(0, peakElementIndex, target)
        partition2 = findElementSecondParition(peakElementIndex + 1, n - 1, target)
        
        if partition1 != -1:
            return partition1
        
        if partition2 != -1:
            return partition2
        
        return -1
