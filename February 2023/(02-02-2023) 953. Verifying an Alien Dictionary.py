class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def check(s1, s2):
            for i in range(max(len(s1), len(s2))):
                try:
                    charA = s1[i]
                except:
                    return True
                try:
                    charB = s2[i]
                except:
                    return False
                if HashMap[charA] < HashMap[charB]:
                    return True
                if HashMap[charA] == HashMap[charB]:
                    continue
                else:
                    return False
            return True
        
        HashMap = dict()
        
        for i in range(len(order)):
            HashMap[order[i]] = i
        
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            if check(a, b):
                continue
            return False
        return True
