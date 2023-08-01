class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
                    
        def traverse(index,currArr):
            if len(currArr)==k:
                res.append(currArr[:])
                return
            
            for i in range(index,n+1):
                traverse(i+1,currArr+[i])
            
        res=[]
        traverse(1,[])
        return res