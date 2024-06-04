class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1={}
        for i in s:
            dict1[i]=1+dict1.get(i,0)
        
        res=0
        flag=0
        for k,v in dict1.items():
            if v%2==0:
                res+=v
            else:
                res+=(v-1)
                if flag==0:
                    flag=1
        
        return res+flag