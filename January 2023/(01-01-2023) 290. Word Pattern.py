class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1={}
        dict2={}
        list1=s.split(" ")
        if len(pattern)!=len(list1):
            return False
        for i in range(len(list1)):
            if pattern[i] not in dict1:
                if list1[i] not in dict1.values():
                    dict1[pattern[i]]=list1[i]
                else:
                    dict1[pattern[i]]=" "
        str1=""
        for i in pattern:
            str1=str1+dict1[i]+" "
        if str1.strip()==s.strip():
            return True
        else:
            return False
