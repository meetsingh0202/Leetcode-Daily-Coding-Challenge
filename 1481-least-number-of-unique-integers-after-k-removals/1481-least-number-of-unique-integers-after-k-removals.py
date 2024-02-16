class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        HashMap = dict()
        
        for i in arr:
            HashMap[i] = 1 + HashMap.get(i, 0)
        
        l = []
        
        for key, val in HashMap.items():
            l.append([key, val])
        
        l.sort(key = lambda x : x[1])
        i = 0
        
        while k:
            currKey, currVal = l[i]
            
            if currVal <= k:
                i += 1
                k -= currVal
            else:
                break
        
        return len(l) - i