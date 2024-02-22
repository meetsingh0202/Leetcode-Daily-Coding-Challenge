class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust==[]:
            return 1
        dict1={}
        everybody=set()
        for i in trust:
            everybody.add(i[0])
            peopletrusted=i[1]
            dict1[peopletrusted]=1+dict1.get(peopletrusted,0)
            
        # print(dict1)
        flag=0
        for key,value in dict1.items():
            if value==n-1:
                if key not in everybody:
                    return key
                    flag=1
        if flag==0:
            return -1
            