class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        allcaps=word.upper()
        if allcaps==word:
            return True
        allsmall=word.lower()
        if allsmall==word:
            return True
        if word.capitalize()==word:
            return True
        return False
