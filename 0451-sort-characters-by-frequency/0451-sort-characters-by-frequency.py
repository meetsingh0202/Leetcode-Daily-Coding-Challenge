class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            if(c in dic):
                dic[c] += 1
            else:
                dic[c] = 1
                
        ordered = sorted(dic, key=dic.get,reverse = True)
        output = ''
        for c in ordered:
            output += c * dic[c]
            
        return output