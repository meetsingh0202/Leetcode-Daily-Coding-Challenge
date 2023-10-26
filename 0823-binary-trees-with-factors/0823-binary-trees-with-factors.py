class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        def traverse(currIndex):
            
            currCount = 1
            for i in range(currIndex):
                tempVal1 = arr[i]
                tempVal2 = arr[currIndex] / tempVal1
                currCount += (memo.get(tempVal1, 0) * memo.get(tempVal2, 0))
            
            memo[arr[currIndex]] = currCount
            return currCount
        
        memo = dict()
        totalCount = 0
        arr.sort()
        MOD = 1000000007
        
        for i in range(len(arr)):
            totalCount += traverse(i) % MOD
        return totalCount % MOD