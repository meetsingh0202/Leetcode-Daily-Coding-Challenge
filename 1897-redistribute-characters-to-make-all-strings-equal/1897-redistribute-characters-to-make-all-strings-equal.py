class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        HashMap = dict()
        totalWords = len(words)
        
        for word in words:
            for char in word:
                HashMap[char] = 1 + HashMap.get(char, 0)
        
        for key, val in HashMap.items():
            if val % totalWords == 0:
                continue
            return False
        
        return True