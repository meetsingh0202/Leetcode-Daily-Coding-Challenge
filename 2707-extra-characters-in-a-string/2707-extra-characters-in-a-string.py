class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def traverse(index):
            if index >= len(s):
                return 0
            
            res = 1 + traverse(index + 1)
            
            for i in range(len(s) - index):
                tempSubString = s[index :index + i + 1]
                if tempSubString in dictionary:
                    res = min(res, traverse(index + i + 1))
            return res
        
        dictionary = set(dictionary)
        return traverse(0)