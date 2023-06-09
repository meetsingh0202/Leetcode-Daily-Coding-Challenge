class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        left = 0
        right = len(letters) - 1
        while left <= right :
            mid = (left + right) // 2
            if target >= letters[mid]:
                left = mid + 1 
            if target < letters[mid]:
                right = mid - 1
        return letters[left]