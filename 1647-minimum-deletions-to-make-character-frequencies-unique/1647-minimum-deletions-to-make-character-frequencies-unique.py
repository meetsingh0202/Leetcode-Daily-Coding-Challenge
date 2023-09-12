class Solution:
    def minDeletions(self, s: str) -> int:
        freq=[0]*26
        
        for i in s:
            freq[ord(i)-ord('a')]+=1
        occured=set()
        count=0
        for i in range(0,26):
            curr=freq[i]
            
            while curr>0:
                if curr in occured:
                    curr-=1
                    count+=1
                else:
                    break
                    
            if curr!=0:
                occured.add(curr)
                
        return count