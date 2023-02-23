class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) >> 1
            if (mid == len(arr) - 1) and arr[mid - 1] != arr[mid]:
                return arr[mid]
            
            if mid == 0 and arr[mid + 1] != arr[mid]:
                return arr[mid]
            
            if (mid + 1 < len(arr) and arr[mid] != arr[mid + 1]) and (mid - 1 >= 0 and arr[mid] != arr[mid - 1]):
                return arr[mid]
            
            if arr[mid] == arr[mid + 1]:
                if mid % 2 == 0:
                    low = mid + 1
                else:
                    high = mid - 1
            elif arr[mid] == arr[mid - 1]:
                if mid % 2 == 0:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1 
                
