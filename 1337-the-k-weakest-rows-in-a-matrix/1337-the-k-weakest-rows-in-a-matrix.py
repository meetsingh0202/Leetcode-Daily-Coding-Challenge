class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        
        def findSoldiers(arr):
            if arr[0] == 0:
                return -1
            
            low = 0
            high = len(arr) - 1
            
            ans = 0
            
            while low <= high:
                mid = (low + high) >> 1
                
                if arr[mid] == 1 and mid + 1 < len(arr) and arr[mid + 1] == 0:
                    return mid
                
                if arr[mid] == 1 and mid == len(arr) - 1:
                    return mid
                
                if arr[mid] == 1:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return low
        
        heap = []
        
        for index, val in enumerate(mat):
            soldiers = findSoldiers(val) + 1
            heappush(heap, (soldiers, index))
        
        res = []
        
        while heap:
            if k:
                k -= 1
                val, index = heappop(heap)
                res.append(index)
            else:
                break
                
        return res