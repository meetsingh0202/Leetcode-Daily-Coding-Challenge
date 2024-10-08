class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0
        
        for word in words:
            flag = 0
            for char in word:
                if char not in allowed:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        
        return count
            