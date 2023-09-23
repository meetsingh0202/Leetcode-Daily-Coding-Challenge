class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache={}
        wordset=set(words)
        
        def find(word):
            if word not in wordset:
                return 0
            
            if word in cache:
                return cache[word]
            else:
                maxlen=0
                for i in range(len(word)):
                    maxlen=max(maxlen,find(word[:i]+word[i+1:])+1)
                cache[word]=maxlen
            
            return maxlen
        
        for word in words:
            find(word)
        
        return max(cache.values())