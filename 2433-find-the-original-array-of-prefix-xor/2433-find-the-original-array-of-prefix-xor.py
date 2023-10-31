class Solution:
    def findArray(self, pref: List[int]) -> List[int]:       
        
        arr = [pref[0]]
        currXor = pref[0]
        
        for i in pref[1:]:
            arr.append(currXor ^ i)
            currXor = currXor ^ (currXor ^ i)
        
        return arr