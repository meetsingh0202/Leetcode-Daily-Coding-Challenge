class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sumM = sum(rolls)
        total_sum = mean * (n + m)
        missing_sum = total_sum - sumM
        base_value = missing_sum // n
        remainder = missing_sum % n

        if base_value <= 0 or base_value > 6 or (base_value == 6 and remainder > 0):
            return []

        result = [base_value] * n
        for i in range(remainder):
            result[i] += 1
        return result
