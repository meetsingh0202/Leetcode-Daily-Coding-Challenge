class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        HashMap = dict()
        count = 0
        MOD = 1000000007
        deliciousness.sort()
        
        for i in deliciousness:
            currNum = i
            
            for k in range(22):
                temp = 1 << k
                
                y = temp - currNum
                
                count += HashMap.get(y, 0)
                count = count % MOD
                
            HashMap[i] = 1 + HashMap.get(i, 0)
            
        return count % MOD