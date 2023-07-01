class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        children = (0, ) * k
        
        @cache
        def traverse(currIndex, children):
            if currIndex == len(cookies):
                return max(children)
            
            currCookies = cookies[currIndex]
            ans = float('inf')
            tempChildren = list(children)
            
            for i in range(k):
                tempChildren[i] += currCookies
                ans = min(ans, traverse(currIndex + 1, tuple(sorted(tempChildren))))
                tempChildren[i] -= currCookies
                
            return ans
        
        return traverse(0, children)
