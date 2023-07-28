class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def traverse(currTurn, firstIndex, lastIndex):
            if firstIndex > lastIndex:
                return 0
            
            if currTurn == 0:
                takeFirst = nums[firstIndex] + traverse(1, firstIndex + 1, lastIndex)
                takeLast = nums[lastIndex] + traverse(1, firstIndex, lastIndex - 1)
                ans = max(takeFirst, takeLast)
            else:
                takeFirst = traverse(0, firstIndex + 1, lastIndex) - nums[firstIndex]
                takeLast = traverse(0, firstIndex, lastIndex - 1) - nums[lastIndex]
                ans = min(takeFirst, takeLast)
            return ans
        
        score = traverse(0, 0, len(nums) - 1)
        return score >= 0