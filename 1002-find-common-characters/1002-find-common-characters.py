class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = []
        for i in words:
            l.append(set(i))
        ans = []
        for i in list(l[0]):
            min = words[0].count(i)
            for j in range(1,len(words)):
                if min>=words[j].count(i):
                    min = words[j].count(i)
            for k in range(min):
                ans.append(i)
        return ans