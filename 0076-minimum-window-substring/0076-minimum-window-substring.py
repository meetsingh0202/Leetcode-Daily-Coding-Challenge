class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        resultindexs=[-1,-1]
        dictoft={}
        for i in t:
            dictoft[i]=1+dictoft.get(i,0)
        required=len(dictoft)
        current=0
        left=0
        window={}
        minlength=float('inf')
        for right in range(len(s)):
            currchar=s[right]
            window[currchar]=1+window.get(currchar,0)
            
            if currchar in dictoft and window[currchar]==dictoft[currchar]:
                current+=1
            
            while current==required:
                currlength=(right-left+1)
                if currlength<minlength:
                    minlength=currlength
                    resultindexs=[left,right]
                window[s[left]]-=1
                if s[left] in dictoft and window[s[left]]<dictoft[s[left]]:
                    current-=1
                left+=1
        
        if resultindexs==[-1,-1]:
            return ""
        return s[resultindexs[0]:resultindexs[1]+1]