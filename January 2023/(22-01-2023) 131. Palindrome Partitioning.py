class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        
        def helper(arr, str):
            if str:
                for i in range(1, len(str)+1):
                    if str[:i] == str[:i][::-1]:
                        helper(arr+[str[:i]], str[i:])
            elif arr: 
                    res.append(arr)
        
        helper([], s)
        return res
