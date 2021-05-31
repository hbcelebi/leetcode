
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

from typing import List
import numpy as np

def largest_row_of_zeros(l):
    c = 0
    max_count = 0
    idx_start = 0
    idx_end = 0
    idx = 0
    if np.sum(l) == 0:
        return len(l), 0, len(l)
    for j in l:
        if j == 0:
            if c == 0:
                idx_start = idx
            c += 1
        else:
            if c > max_count:
                max_count = c
                idx_end = idx
            c = 0
        idx += 1
    return max_count, idx_start, idx_end

### Here starts my code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        s_temp = []
        idx_start = 0
        idx_end = 0
        for character in s:
            s_temp.append(ord(character))
        s_rev = s_temp[::-1]
        for n in range(len(s)):
            temp_len, idx_start_tmp, idx_end_temp = largest_row_of_zeros(np.abs(np.subtract(s_temp[0:len(s_temp)-n], 
                                                                      s_rev[n:len(s_temp)])))
            print(s_temp[0:len(s_temp)-n])
            print(s_rev[n:len(s_temp)])
            print(temp_len, idx_start_tmp, idx_end_temp)
            if temp_len > max_len:
                max_len = temp_len
                idx_start = idx_start_tmp
                idx_end = idx_end_temp
            
            temp_len, idx_start_tmp, idx_end_temp = largest_row_of_zeros(np.abs(np.subtract(s_temp[n:len(s_temp)], 
                                                                      s_rev[0:len(s_temp)-n])))
            print(s_temp[0:len(s_temp)-n])
            print(s_rev[n:len(s_temp)])
            print(temp_len, idx_start_tmp, idx_end_temp)
            if temp_len > max_len:
                max_len = temp_len
                idx_start = n+idx_start_tmp
                idx_end = n+idx_end_temp

        return s[idx_start:idx_end]
            
s = Solution()
result = s.longestPalindrome("aacabdkacaa")
print(result)
        
result = s.longestPalindrome("aaaabaaa")
print(result)

        