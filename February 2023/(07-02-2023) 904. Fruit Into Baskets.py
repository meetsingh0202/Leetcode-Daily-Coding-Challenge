class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        HashMap = dict()
        Max = 0
        l = 0
        for r in range(len(fruits)):
            HashMap[fruits[r]] = 1 + HashMap.get(fruits[r], 0)
            if len(HashMap) > 2:
                HashMap[fruits[l]] -= 1
                if HashMap[fruits[l]] == 0:
                    del HashMap[fruits[l]]
                l += 1
            else:
                Max = max(Max, r - l + 1)
        return Max
