class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for number in arr:
            if number % 2 != 0:
                odd_count += 1
                if odd_count == 3: return True
            else:
                odd_count = 0
        return False