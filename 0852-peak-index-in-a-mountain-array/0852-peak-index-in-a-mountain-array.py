class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        low = 0
        high = len(arr)
        
        while low < high:
            mid = (low + high) >> 1
            if (arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]):
                return mid
            if (arr[mid] < arr[mid + 1]):
                low = mid
            else:
                high = mid
        