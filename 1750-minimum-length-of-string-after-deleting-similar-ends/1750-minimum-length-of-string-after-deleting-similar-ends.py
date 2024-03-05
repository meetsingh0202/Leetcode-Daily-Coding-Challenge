class Solution:
    def minimumLength(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        left, right = 0, len(s) - 1
        
        tempSet = set()
        
        while left < right:
            a, b = s[left], s[right]
            
            if a == b:
                while left <= right and s[left] == a:
                    left += 1
                while right >= left and s[right] == b:
                    right -= 1
            else:
                break
        
        return right - left + 1