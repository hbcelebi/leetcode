
"""
Created on Mon Jun 2 18:45:28 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

class Solution:
def isSubsequence(self, s: str, t: str) -> bool:
    m = len(s)
    idx = 0
    if m == 0:
        return True
    # loop over the long string and check if the value is in the substring
    for value in t:
        if value == s[idx]:
            idx += 1
        # if we are already at the end of the substring return True
        if idx == m:
            return True
    # return True if we reach the end of substring
    return idx == m
            
s = Solution()
array = "ahbgdc"
sequence = "axc"
print(isSubsequence(array, sequence))
        
