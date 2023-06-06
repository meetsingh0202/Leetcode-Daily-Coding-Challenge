class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        lastDiff = abs(arr[0] - arr[1])
        
        for i in range(1, len(arr) - 1):
            currDiff = abs(arr[i] - arr[i + 1])
            if currDiff == lastDiff:
                continue
            return False
        
        return True