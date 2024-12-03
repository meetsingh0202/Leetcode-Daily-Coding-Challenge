class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        count = 0
        word_idx = []
        for idx, word in enumerate(sentence):
            if word.startswith(searchWord):
                count +=1
                word_idx.append(idx + 1)
        if count == 0:
            return -1
        else:
            return word_idx[0]
