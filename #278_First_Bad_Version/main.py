
"""
Created on Mon May  3 14:40:08 2021

@author: hbc
"""

# This is a O(N) computational complexity and O(1) space complexity solution to the problem
from typing import List

def isBadVersion(version):
    first_bad_version = 4
    return version >= first_bad_version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        # I will use binary search
        # initialize the indexes
        left_idx = 1
        right_idx = n
        version = 0
        # do a first check
        if(n == 1):
            return 1
        # search in a loop
        while(left_idx <= right_idx):
            # set the mid_index to the middle
            version = int((left_idx + right_idx)/2)
            # if the value at mid_idx is true (TRUE = IT IS BAD VERSION)
            if(isBadVersion(version) == True and isBadVersion(version-1) == False):
                return version
            elif(isBadVersion(version) == True):
                right_idx = version - 1
            else:
                left_idx = version + 1
        return version
            
        
            
s = Solution()
result = s.firstBadVersion(4)
print(result)
        
        