# https://leetcode.com/problems/count-primes


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[:2] = [False, False]
        for i in range(int((n - 1)**0.5) + 1):
            if is_prime[i]:
                is_prime[i**2::i] = [False] * len(is_prime[i**2::i])
        return is_prime.count(True)
