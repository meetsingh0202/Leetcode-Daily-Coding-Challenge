class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = int(math.log(n, 2))
        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n - 2 ** k)