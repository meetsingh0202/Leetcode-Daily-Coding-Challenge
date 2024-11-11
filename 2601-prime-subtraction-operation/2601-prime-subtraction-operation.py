class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n+1)
            is_prime[0] = is_prime[1] = False
            for p in range(2, int(n**0.5)+1):
                if is_prime[p]:
                    for i in range(p*p, n+1, p):
                        is_prime[i] = False
            for i in range(2, n+1):
                if is_prime[i]:
                    primes.append(i)
        
        primes = list()
        sieve_of_eratosthenes(1001)
        primes = primes[::-1]
        
        for i in range(len(nums)):
            for k in primes:
                if i == 0:
                    if nums[i] - k > 0:
                        nums[i] -= k
                        break
                        
                elif nums[i] - k > 0 and nums[i] - k > nums[i - 1]:
                    nums[i] -= k
                    break
                    
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True
            