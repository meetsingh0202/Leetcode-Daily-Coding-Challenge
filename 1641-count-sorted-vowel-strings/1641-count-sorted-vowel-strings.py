class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        pair = {'a' : {'a', 'e', 'i', 'o', 'u'}, 'e' : {'e', 'i', 'o', 'u'}, 'i' : {'i', 'o', 'u'}, 'o' : {'o', 'u'}, 'u' :'u'}
        
        @cache
        def traverse(currIndex, currCharacter):
            if currIndex == n:
                return 1
            
            count = 0
            for i in pair[currCharacter]:
                count += traverse(currIndex + 1, i)
            
            return count
        
        return traverse(0, 'a')