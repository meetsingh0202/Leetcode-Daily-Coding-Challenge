class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        def getFreq(word):
            vals = []
            HashMap = dict()
            for i in word:
                HashMap[i] = 1 + HashMap.get(i, 0)
            for key, val in HashMap.items():
                vals.append(val)
            return sorted(vals)
        
        return set(word1) == set(word2) and getFreq(word1) == getFreq(word2)
