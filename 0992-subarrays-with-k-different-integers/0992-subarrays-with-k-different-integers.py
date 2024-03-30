class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        counter = dict()
        res = 0
        left = 0
        for right in range(len(A)):
            counter[A[right]] = counter.get(A[right], 0) + 1
            while len(counter) > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    counter.pop(A[left])
                left += 1
            res += right - left + 1
        return res
