class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        HashMap = dict()
        
        res = 0
        left = 0
        
        for right in range(len(s)):
            
            currChar = s[right]
            HashMap[currChar] = 1 + HashMap.get(currChar, 0)
            
            if len(HashMap) == right - left + 1:
                res = max(res, right - left + 1)
            
            else:
                while left <= right and len(HashMap) < right - left + 1:
                    
                    HashMap[s[left]] -= 1
                    
                    if HashMap[s[left]] == 0:
                        del HashMap[s[left]]
                        
                    left += 1
        
        return res
                
                