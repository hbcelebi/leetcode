
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The idea is to find all the non-prime numbers in the array
        if n <= 2:
            return 0
        if n == 3:
            return 1
        # intialize the array
        is_prime = n*[True]
        # 0 and 1 are not prime
        is_prime[0] = is_prime[1] = False
        # numbers that are divisible to 2 are not prime
        is_prime[0::2] = len(is_prime[0::2])*[False]
        # but 2 is prime
        is_prime[2] = True
        # numbers that are divisible to 3 are not prime
        is_prime[0::3] = len(is_prime[0::3])*[False]
        # but 3 is prime
        if(n > 3):
            is_prime[3] = True
        # set the rest non-prime numbers inside a loop
        for idx in range(5,int(math.sqrt(n))+1,2):
            if(is_prime[idx]):
                for idx_multiples in range(2*idx, n, idx):
                    is_prime[idx_multiples] = False
        #print(is_prime)
        return sum(is_prime)
            
s = Solution()
result = s.countPrimes(10)
print(result)
        
        