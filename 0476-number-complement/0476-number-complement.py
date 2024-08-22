class Solution:
    def findComplement(self, num: int) -> int:
        l=[]
        str1=bin(num)[2:]
        l=list(str1)
        for i in range(len(l)):
            if l[i]=='1':
                l[i]='0'
            elif l[i]=='0':
                l[i]='1'
        str2="".join(l)
        x=int(str2,2)
        return (x)