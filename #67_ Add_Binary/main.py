
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_carry = 0
        str_result = []
        len_a, len_b = len(a)-1, len(b)-1
        
        # do the binary adition inside the loop
        while len_a >= 0 or len_b >= 0:
            num_sum = num_carry
            if len_a >= 0:
                num_sum += int(a[len_a])
                len_a -= 1
            if len_b >= 0:
                num_sum += int(b[len_b])
                len_b -= 1
            # update the carry 
            num_carry = num_sum // 2
            # append the binary result
            str_result.append(str(num_sum%2))
        
        # the loop is done. if carry = 1, append it
        if num_carry:
            str_result.append(str(1))
        
        # reverse the list and convert it to string and return 
        return ''.join(reversed(str_result))
        
        
            
s = Solution()
result = s.addBinary("1010", "1011")
print(result)
        

        