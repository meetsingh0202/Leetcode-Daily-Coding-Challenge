class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        def findMaximum(currVal):
            low = 0
            ans = -1
            high = len(arr) - 1
            
            while low <= high:
                mid = (low + high) >> 1

                if arr[mid][0] < currVal:
                    ans = mid
                    low = mid + 1
                
                elif arr[mid][0] == currVal:
                    return mid                                        
                
                else:
                    high = mid - 1
            
            return ans
                
        items.sort(key = lambda x : (x[0], -x[1]))
        
        arr = []
        currMax = 0
        
        for i in items:
            price, beauty = i
            currMax = max(currMax, beauty)

            if len(arr) > 0:
                if arr[-1][0] == price:
                    continue
                else:
                    arr.append([price, currMax])
            else:
                arr.append([price, currMax])
        
        res = []
        
        for i in queries:
            ansIndex = findMaximum(i)
            
            if ansIndex == -1:
                res.append(0)
            else:
                res.append(arr[ansIndex][1])
        
        return res