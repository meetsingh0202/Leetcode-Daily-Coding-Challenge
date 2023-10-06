class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def traverse(num, currSum):
            if num == 1:
                return 1

            notPick = traverse(num - 1, currSum)
            Pick = 0
            if currSum >= num:
                Pick = num * traverse(num, currSum - num)
            return max(Pick, notPick)
        
        return traverse(n - 1, n)