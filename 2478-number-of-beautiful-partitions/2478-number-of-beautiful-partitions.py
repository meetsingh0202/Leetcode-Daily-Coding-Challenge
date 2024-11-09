class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        
        @cache
        def traverse(currIndex, k, flag):
            if k < 0:
                return 0
            
            if currIndex == len(s) and k == 0:
                return 1
            
            if currIndex >= len(s) or k == 0:
                return 0
            
            currElement = s[currIndex]
            
            if not flag:
                if s[currIndex] not in prime:
                    return 0
                
                return traverse(currIndex + minLength - 1, k, True)
            
            else:
                newPartition, oldPartition = 0, 0
                
                if s[currIndex] in nonPrime:
                    newPartition = traverse(currIndex + 1, k - 1, False)
                
                oldPartition = traverse(currIndex + 1, k, flag)
                
                return newPartition + oldPartition
        
        prime = {'2', '3', '5', '7'}
        nonPrime = {'0', '1', '4', '6', '8', '9'}
        MOD = 10**9 + 7
        
        if s[0] not in prime or s[-1] not in nonPrime:
            return 0
        
        return traverse(0, k, False) % MOD