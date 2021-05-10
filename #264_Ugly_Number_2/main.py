
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

from typing import List


def isUgly(n):
    # if the number is less than 1 it is ugly
    if n < 1:
        return False
    # set the ugly dividers
    ugly_dividers = [2, 3, 5]
    # divide the number to the ugly dividers until the number is not divisable anymore
    for div in ugly_dividers:
        while n%div == 0:
            n //= div
    # return True if n is 1 (if not, there are other dividers and the number is not ugly)
    return n == 1

class Solution(object):
    def nthUglyNumber(self, n):
        number = 0
        counter = 0
        while 1:
            if isUgly(number):
                counter += 1
                if counter == n:
                    break
            number += 1
        return number
                
                
        
            
s = Solution()
result = s.nthUglyNumber(1000)
print(result)
        

