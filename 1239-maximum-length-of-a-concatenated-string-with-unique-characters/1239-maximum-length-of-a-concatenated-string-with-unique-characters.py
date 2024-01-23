class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res=0
        def backtrack(start,arr,word):
            if len(word)==len(set(word)):
                self.res=max(self.res,len(word))
            else:
                return
            for i in range(start,len(arr)):
                backtrack(i+1,arr,word+arr[i])
        
        backtrack(0,arr,"")
        return self.res